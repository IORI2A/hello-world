
//#include "..\..\stdafx.h"
//#include "..\include\Tool.h"

// 在项目属性中配置引用的头文件的所在目录位置： 配置属性 > C/C++ > 常规 > 附加包含目录 。以简化 #include 语句的编写。
#include "stdafx.h"
#include "lz_window_helper.h"

#include "lz_tool.h"

/*
可通过窗口标题来查找匹配的窗口，获取取句柄。
FindWindow 的 lpWindowName 来指定窗口的标题文体(title) 。

*/

// 使用 linux 风格的命名方式。
void my_find_window()
{
	// 搜索： 向另一个进行发送窗口消息
	// [如何向另外一个进程的窗口里面的一个按钮发送点击消息](https://zhidao.baidu.com/question/2014210690670358308.html)
	// [MFC 向指定窗口发送自定义消息](https://blog.csdn.net/penpenandtongtong/article/details/18598907)
	// [向某个窗口发送按键消息(包括后台隐藏的窗口)](https://blog.csdn.net/qiangzi4646/article/details/79492497)

	HWND fined_window_handle = lz_find_window(NULL, TEXT("白名单数据库管理软件"));

	HWND fined_button_handle = lz_find_window_ex(fined_window_handle, NULL, NULL, TEXT("注册"));

	// "#32770" 是什么意思
	//HWND fined_window_handle = lz_find_window(TEXT("#32770"), TEXT("注册"));

	BOOL bool_set_foreground_window = lz_set_foreground_window(fined_window_handle);

	// 销毁无效果。 2019-12-17
	//DestroyWindow(fined_window_handle);
	// 使用 WM_CLOSE 消息可以关闭窗口。
	//SendMessage(fined_window_handle, WM_CLOSE, 0, 0);

	// 间隔性的一次有效，一次无效。
	// 针对该问题，搜索： SendMessage 模拟鼠标点击 无效
	// [sendmessage()模拟鼠标点击](https://www.cnblogs.com/mvc2014/p/3775967.html)
	// [sendmessage发送模拟点击按钮没有反应](https://bbs.csdn.net/topics/391832951)
	// + SetForegroundWindow
	//SendMessage(fined_button_handle, WM_LBUTTONDOWN, 0, 0);
	//// 目前测试休息时间可有可无。 2019-12-17
	////Sleep(200);
	//SendMessage(fined_button_handle, WM_LBUTTONUP, 0, 0);

	// PostMessage 发了消息不用等待处理，直接返回。
	// 测试也有效果。  2019-12-17
	BOOL bool_post_message = 0;
	bool_post_message = PostMessage(fined_button_handle, WM_LBUTTONDOWN, 0, 0);
	bool_post_message = PostMessage(fined_button_handle, WM_LBUTTONUP, 0, 0);

	// 直接向窗口发送鼠标按键消息，没有任何反应。 2019-12-17
	//BOOL bool_post_message = 0;
	//bool_post_message = PostMessage(fined_window_handle, WM_LBUTTONDOWN, 0, 0);
	//bool_post_message = PostMessage(fined_window_handle, WM_LBUTTONUP, 0, 0);
}


// 搜索： 按键精灵
// 搜索： 按键精灵 源码
// 搜索： 按键精灵 原理
// 搜索： 按键精灵 Q语言

// [按键精灵和TC的比较](https://zhidao.baidu.com/question/358220154.html)
// [按键精灵](https://www.zhihu.com/topic/19656165/hot)
// [按键精灵的工作原理是什么？](https://zhidao.baidu.com/question/12234875.html)
// [Q语言 （脚本语言）](https://baike.baidu.com/item/Q%E8%AF%AD%E8%A8%80/1398393)


///////////////////////////////////////////////////////////////////////////////////////////////////////
// 对 WIN32 API 进行简单封装，参数和返回值保持与原函数相同，主要是为了提供日志调试记录。
// 命名使用 linux 风格的命名方式，以 lz 开关(同时方便IDE的智能提示)，后接原函数的小写同名。
// 倒序增加封装函数。
///////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////
//Win32 and COM Development 
//User Interface 
//Windows User Experience
//Windows Management
//Windows User Interface 
//Windowing 
//Windows 

BOOL lz_set_foreground_window(HWND hWnd)
{
	TOOL_AUTO_LOG_FUNCTION_INFO();

	// 将窗口置前( Z 轴最上层)，并激活窗口可接收用户交互。
	BOOL bool_set_foreground_window = SetForegroundWindow(hWnd);
	if (bool_set_foreground_window)
	{
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("bool_set_foreground_window = %d", bool_set_foreground_window);
	}
	else
	{
		char error_infor[256] = {};
		DWORD error_code = Tool::GetLastErrorCodeAndText_A(error_infor, sizeof(error_infor));
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("bool_set_foreground_window = %d, LastError: [%d] %s"
			, bool_set_foreground_window, error_code, error_infor);
	}

	return bool_set_foreground_window;
}

HWND lz_find_window_ex(HWND hwndParent, HWND hwndChildAfter, LPCTSTR lpszClass, LPCTSTR lpszWindow)
{
	TOOL_AUTO_LOG_FUNCTION_INFO();

	// FindWindow 通过指参数进行查找，获取匹配的顶层窗口(top-level window)。
	// 不查找子窗口。
	// 当多个窗口的标题同名时，应该是取得的 Z 轴最上层的那个。
	HWND fined_window_handle = FindWindowEx(hwndParent, hwndChildAfter, lpszClass, lpszWindow);
	if (fined_window_handle)
	{
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = %08X", fined_window_handle);
	}
	else
	{
		char error_infor[256] = {};
		DWORD error_code = Tool::GetLastErrorCodeAndText_A(error_infor, sizeof(error_infor));
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = %08X, LastError: [%d] %s"
			, fined_window_handle, error_code, error_infor);
	}

	return fined_window_handle;
}

HWND lz_find_window(LPCTSTR lpClassName, LPCTSTR lpWindowName)
{
	TOOL_AUTO_LOG_FUNCTION_INFO();

	HWND fined_window_handle = FindWindow(lpClassName, lpWindowName);
	if (fined_window_handle)
	{
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = %08X", fined_window_handle);
	}
	else
	{
		char error_infor[256] = {};
		DWORD error_code = Tool::GetLastErrorCodeAndText_A(error_infor, sizeof(error_infor));
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = %08X, LastError: [%d] %s"
			, fined_window_handle, error_code, error_infor);
	}

	return fined_window_handle;
}

