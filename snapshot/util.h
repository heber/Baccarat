#pragma once
#include "stdafx.h"
#include <tlhelp32.h> 

// convert widechar string to multibyte with default ANSI code
void WideChar2MultiByte(
    const wchar_t *wstr, char *acp_str)
{
    int nACPLen = WideCharToMultiByte(
        CP_ACP, 0, wstr, -1, NULL, 0, NULL, NULL);
    WideCharToMultiByte(CP_ACP, 0, wstr,
        -1, acp_str, nACPLen, NULL, NULL);
}

bool hasProcesses(const char *pname, DWORD &pid)
{
    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(pe32);
    //给系统内所有的进程拍个快照 
    HANDLE hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hProcessSnap == INVALID_HANDLE_VALUE)
        return false;

    //遍历进程快照，轮流显示每个进程的信息 
    BOOL bMore = Process32First(hProcessSnap, &pe32);
    char value[256] = { 0 };
    //关闭进程的间隔时间
    while (bMore)
    {
		WideChar2MultiByte(pe32.szExeFile, value);
        if (strcmp(value, pname) == 0)
        {
            pid = pe32.th32ProcessID;
            return true;
            //KillProcess(pe32.th32ProcessID);
            //printf("%s has been shutdown the %dth time.\n", pe32.szExeFile, ++shutdownCount);
        }
        bMore = Process32Next(hProcessSnap, &pe32);
    }
    //不要忘记清除掉snapshot对象 
    CloseHandle(hProcessSnap);
    return false;
}


struct handle_data {
    unsigned long process_id;
    HWND best_handle;
};


BOOL is_main_window(HWND handle)
{
    return GetWindow(handle, GW_OWNER) == (HWND)0 && IsWindowVisible(handle);
}

BOOL CALLBACK enum_windows_callback(HWND handle, LPARAM lParam)
{
    handle_data& data = *(handle_data*)lParam;
    unsigned long process_id = 0;
    GetWindowThreadProcessId(handle, &process_id);
    if (data.process_id != process_id || !is_main_window(handle)) {
        return TRUE;
    }
    data.best_handle = handle;
    return FALSE;
}

HWND find_main_window(unsigned long process_id)
{
    handle_data data;
    data.process_id = process_id;
    data.best_handle = 0;
    EnumWindows(enum_windows_callback, (LPARAM)&data);
    return data.best_handle;
}
