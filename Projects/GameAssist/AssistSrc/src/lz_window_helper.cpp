
//#include "..\..\stdafx.h"
//#include "..\include\Tool.h"

// ����Ŀ�������������õ�ͷ�ļ�������Ŀ¼λ�ã� �������� > C/C++ > ���� > ���Ӱ���Ŀ¼ ���Լ� #include ���ı�д��
#include "stdafx.h"
#include "lz_window_helper.h"

#include "lz_tool.h"

/*
��ͨ�����ڱ���������ƥ��Ĵ��ڣ���ȡȡ�����
FindWindow �� lpWindowName ��ָ�����ڵı�������(title) ��

*/

// ʹ�� linux ����������ʽ��
void my_find_window()
{
	// ������ ����һ�����з��ʹ�����Ϣ
	// [���������һ�����̵Ĵ��������һ����ť���͵����Ϣ](https://zhidao.baidu.com/question/2014210690670358308.html)
	// [MFC ��ָ�����ڷ����Զ�����Ϣ](https://blog.csdn.net/penpenandtongtong/article/details/18598907)
	// [��ĳ�����ڷ��Ͱ�����Ϣ(������̨���صĴ���)](https://blog.csdn.net/qiangzi4646/article/details/79492497)

	HWND fined_window_handle = lz_find_window(NULL, TEXT("���������ݿ�������"));

	HWND fined_button_handle = lz_find_window_ex(fined_window_handle, NULL, NULL, TEXT("ע��"));

	// "#32770" ��ʲô��˼
	//HWND fined_window_handle = lz_find_window(TEXT("#32770"), TEXT("ע��"));

	BOOL bool_set_foreground_window = lz_set_foreground_window(fined_window_handle);

	// ������Ч���� 2019-12-17
	//DestroyWindow(fined_window_handle);
	// ʹ�� WM_CLOSE ��Ϣ���Թرմ��ڡ�
	//SendMessage(fined_window_handle, WM_CLOSE, 0, 0);

	// ����Ե�һ����Ч��һ����Ч��
	// ��Ը����⣬������ SendMessage ģ������� ��Ч
	// [sendmessage()ģ�������](https://www.cnblogs.com/mvc2014/p/3775967.html)
	// [sendmessage����ģ������ťû�з�Ӧ](https://bbs.csdn.net/topics/391832951)
	// + SetForegroundWindow
	//SendMessage(fined_button_handle, WM_LBUTTONDOWN, 0, 0);
	//// Ŀǰ������Ϣʱ����п��ޡ� 2019-12-17
	////Sleep(200);
	//SendMessage(fined_button_handle, WM_LBUTTONUP, 0, 0);

	// PostMessage ������Ϣ���õȴ�����ֱ�ӷ��ء�
	// ����Ҳ��Ч����  2019-12-17
	BOOL bool_post_message = 0;
	bool_post_message = PostMessage(fined_button_handle, WM_LBUTTONDOWN, 0, 0);
	bool_post_message = PostMessage(fined_button_handle, WM_LBUTTONUP, 0, 0);

	// ֱ���򴰿ڷ�����갴����Ϣ��û���κη�Ӧ�� 2019-12-17
	//BOOL bool_post_message = 0;
	//bool_post_message = PostMessage(fined_window_handle, WM_LBUTTONDOWN, 0, 0);
	//bool_post_message = PostMessage(fined_window_handle, WM_LBUTTONUP, 0, 0);
}


// ������ ��������
// ������ �������� Դ��
// ������ �������� ԭ��
// ������ �������� Q����

// [���������TC�ıȽ�](https://zhidao.baidu.com/question/358220154.html)
// [��������](https://www.zhihu.com/topic/19656165/hot)
// [��������Ĺ���ԭ����ʲô��](https://zhidao.baidu.com/question/12234875.html)
// [Q���� ���ű����ԣ�](https://baike.baidu.com/item/Q%E8%AF%AD%E8%A8%80/1398393)


///////////////////////////////////////////////////////////////////////////////////////////////////////
// �� WIN32 API ���м򵥷�װ�������ͷ���ֵ������ԭ������ͬ����Ҫ��Ϊ���ṩ��־���Լ�¼��
// ����ʹ�� linux ����������ʽ���� lz ����(ͬʱ����IDE��������ʾ)�����ԭ������Сдͬ����
// �������ӷ�װ������
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

	// ��������ǰ( Z �����ϲ�)��������ڿɽ����û�������
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

	// FindWindow ͨ��ָ�������в��ң���ȡƥ��Ķ��㴰��(top-level window)��
	// �������Ӵ��ڡ�
	// ��������ڵı���ͬ��ʱ��Ӧ����ȡ�õ� Z �����ϲ���Ǹ���
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

