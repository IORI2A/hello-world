
// GameAssistDlg.cpp : implementation file
//

#include "stdafx.h"
#include "GameAssist.h"
#include "GameAssistDlg.h"

#include "lz_tool.h"
#include "lz_window_helper.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
END_MESSAGE_MAP()


// CGameAssistDlg dialog




CGameAssistDlg::CGameAssistDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CGameAssistDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CGameAssistDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CGameAssistDlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDOK, &CGameAssistDlg::OnBnClickedOk)
	ON_BN_CLICKED(IDCANCEL, &CGameAssistDlg::OnBnClickedCancel)
	ON_WM_DESTROY()
END_MESSAGE_MAP()


// CGameAssistDlg message handlers

BOOL CGameAssistDlg::OnInitDialog()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("创建对话框！");

	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here
	my_find_window();

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CGameAssistDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CGameAssistDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CGameAssistDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



void CGameAssistDlg::OnBnClickedOk()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，调用 OnCancel ，实现与其一样的操作！");

	// TODO: Add control notification handler code here
	//CDialog::OnOK();

	// 【确定】也与【取消】一样结束程序。
	CGameAssistDlg::OnCancel();
}


void CGameAssistDlg::OnBnClickedCancel()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，调用 OnCancel ，最终安全结束程序！");

	// TODO: Add control notification handler code here
	CDialog::OnCancel();
}

//【取消】、【关闭】按钮的默认实现会联动到 OnCancel 。
// MSDN : 
// When you implement a modeless dialog box, always override the OnCancel member function and call DestroyWindow from within it. 
// Don't call the base class CDialog::OnCancel, because it calls EndDialog, which will make the dialog box invisible but will not destroy it.
// You should also override PostNcDestroy for modeless dialog boxes in order to delete this, since modeless dialog boxes are usually allocated with new. Modal dialog boxes are usually constructed on the frame and do not need PostNcDestroy cleanup. 
void CGameAssistDlg::OnCancel()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，准备结束程序，触发销毁窗口消息，联动后续一系列清理操作！");

	// TODO: Add private code and/or call base classes here

	// 当要触发销毁窗口时，就不要调用基类的 OnCancel 方法。
	//CDialog::OnCancel();

	// 手动调用联动实现销毁窗口
	// MSDN:
	// It sends WM_DESTROY and WM_NCDESTROY messages to the window. It does not destroy the CWnd object. 
	// DestroyWindow 发出 WM_DESTROY 和 WM_NCDESTROY 消息，触发销毁窗口。但不会删除窗口C++对象。
	DestroyWindow();
}

// 在窗口被销毁后，PostNcDestroy 被 OnNcDestroy 方法调用。 
// 通过重载 PostNcDestroy，提供删除窗口C++对象的代码。
void CGameAssistDlg::PostNcDestroy()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，删除窗口C++对象！");

	// TODO: Add private code and/or call base classes here
	// 窗口销毁后，还需要删除窗口C++对象。
	delete this;

	CDialog::PostNcDestroy();
}

// 【确定】、【取消】、【关闭】按钮的默认实现动作都未触发 WM_DESTROY 消息。
void CGameAssistDlg::OnDestroy()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，说明窗口正在被销毁，销毁完成后，也通知本程序的退出。！");

	CDialog::OnDestroy();

	// TODO: Add message handler code here
	//此程序中，对话框窗口的销毁也就代表着程序的退出。
	PostQuitMessage(0);
}
