
// GameAssistDlg.cpp: 实现文件
//

#include "stdafx.h"
#include "GameAssist.h"
#include "GameAssistDlg.h"
#include "afxdialogex.h"

#include "AssistSrc/include/Tool.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 用于应用程序“关于”菜单项的 CAboutDlg 对话框

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 对话框数据
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 支持

// 实现
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CGameAssistDlg 对话框



CGameAssistDlg::CGameAssistDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_GAMEASSIST_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CGameAssistDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CGameAssistDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDOK, &CGameAssistDlg::OnBnClickedOk)
	ON_BN_CLICKED(IDCANCEL, &CGameAssistDlg::OnBnClickedCancel)
	ON_WM_DESTROY()
END_MESSAGE_MAP()


// CGameAssistDlg 消息处理程序

BOOL CGameAssistDlg::OnInitDialog()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("创建对话框！");

	CDialogEx::OnInitDialog();

	// 将“关于...”菜单项添加到系统菜单中。

	// IDM_ABOUTBOX 必须在系统命令范围内。
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
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

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作
	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO: 在此添加额外的初始化代码

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
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
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CGameAssistDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CGameAssistDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



void CGameAssistDlg::OnBnClickedOk()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，调用 OnCancel ，实现与其一样的操作！");

	// TODO: 在此添加控件通知处理程序代码
	//CDialogEx::OnOK();

	// 【确定】也与【取消】一样结束程序。
	CGameAssistDlg::OnCancel();
}


void CGameAssistDlg::OnBnClickedCancel()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，调用 OnCancel ，最终安全结束程序！");

	// TODO: 在此添加控件通知处理程序代码
	CDialogEx::OnCancel();
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

	// TODO: 在此添加专用代码和/或调用基类

	// 当要触发销毁窗口时，就不要调用基类的 OnCancel 方法。
	//CDialogEx::OnCancel();

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

	// TODO: 在此添加专用代码和/或调用基类
	// 窗口销毁后，还需要删除窗口C++对象。
	delete this;

	CDialogEx::PostNcDestroy();
}

// 【确定】、【取消】、【关闭】按钮的默认实现动作都未触发 WM_DESTROY 消息。
void CGameAssistDlg::OnDestroy()
{
	TOOL_AUTO_LOG_FUNCTION_INFO();
	CTool::LOG_TO_DEFAULT_FILE_FORMAT_STR_ENDL("进入此处，说明窗口正在被销毁，销毁完成后，也通知本程序的退出。！");

	CDialogEx::OnDestroy();

	// TODO: 在此处添加消息处理程序代码
	//此程序中，对话框窗口的销毁也就代表着程序的退出。
	PostQuitMessage(0);
}
