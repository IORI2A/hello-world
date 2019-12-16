

//#include "..\..\stdafx.h"
//#include "..\include\Tool.h"

// 在项目属性中配置引用的头文件的所在目录位置： 配置属性 > C/C++ > 常规 > 附加包含目录 。以简化 #include 语句的编写。
#include "stdafx.h"
#include "Tool.h"

/*
可通过窗口标题来查找匹配的窗口，获取取句柄。
FindWindow 的 lpWindowName 来指定窗口的标题文体(title) 。

*/

void my_find_window()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	
	// FindWindow 通过指参数进行查找，获取匹配的顶层窗口(top-level window)。
	// 不查找子窗口。
	//HWND fined_window_handle = FindWindow(NULL, TEXT("Circle"));
	HWND fined_window_handle = FindWindow(NULL, TEXT("《梦幻西游》手游"));
	if (fined_window_handle)
	{
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = %08X", fined_window_handle);
	}
	else
	{
		//CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = NULL");

		char error_infor[256] = {};
		DWORD error_code = Tool::GetLastErrorCodeAndText_A(error_infor, sizeof(error_infor));
		CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("fined_window_handle = NULL, LastError: [%d] %s", error_code, error_infor);
	}
}

