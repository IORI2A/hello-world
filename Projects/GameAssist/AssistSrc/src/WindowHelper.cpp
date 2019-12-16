

//#include "..\..\stdafx.h"
//#include "..\include\Tool.h"

// ����Ŀ�������������õ�ͷ�ļ�������Ŀ¼λ�ã� �������� > C/C++ > ���� > ���Ӱ���Ŀ¼ ���Լ� #include ���ı�д��
#include "stdafx.h"
#include "Tool.h"

/*
��ͨ�����ڱ���������ƥ��Ĵ��ڣ���ȡȡ�����
FindWindow �� lpWindowName ��ָ�����ڵı�������(title) ��

*/

void my_find_window()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	
	// FindWindow ͨ��ָ�������в��ң���ȡƥ��Ķ��㴰��(top-level window)��
	// �������Ӵ��ڡ�
	//HWND fined_window_handle = FindWindow(NULL, TEXT("Circle"));
	HWND fined_window_handle = FindWindow(NULL, TEXT("���λ����Ρ�����"));
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

