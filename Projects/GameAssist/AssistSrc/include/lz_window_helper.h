#pragma once

void my_find_window();

///////////////////////////////////////////////////////////////////////////////////////////////////////
BOOL lz_set_foreground_window(HWND hWnd);
HWND lz_find_window_ex(HWND hwndParent, HWND hwndChildAfter, LPCTSTR lpszClass, LPCTSTR lpszWindow);
HWND lz_find_window(LPCTSTR lpClassName, LPCTSTR lpWindowName);
