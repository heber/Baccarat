// Baccarat.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "util.h"

int main()
{
    DWORD pid = 0;
    if (!hasProcesses("notepad.exe", pid))
        return 0;

    HWND hwnd = find_main_window(pid);

    RECT rect;
    ::GetWindowRect(hwnd, &rect);

    int w = rect.right - rect.left;
    int h = rect.bottom - rect.top;

    HDC hdc = ::GetWindowDC(hwnd);
    HDC hdcCompatible = ::CreateCompatibleDC(hdc);
    HBITMAP	hbm = ::CreateCompatibleBitmap(hdc, w, h);
    ::SelectObject(hdcCompatible, hbm);

    unsigned char * data = new unsigned char[w*h * 3];

    BITMAPINFO infoHeader;
    memset(&infoHeader, 0, sizeof(BITMAPINFO));
    infoHeader.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
    infoHeader.bmiHeader.biWidth = w;
    infoHeader.bmiHeader.biHeight = h;
    infoHeader.bmiHeader.biPlanes = 1;
    infoHeader.bmiHeader.biBitCount = 24;
    infoHeader.bmiHeader.biCompression = BI_RGB;

    BITMAPFILEHEADER fileHeader;
    fileHeader.bfType = (WORD)'B' | ((WORD)'M' << 8);
    fileHeader.bfSize = 54 + w*h * 3;
    fileHeader.bfReserved1 = fileHeader.bfReserved2 = 0;
    fileHeader.bfOffBits = 54;
    int count = 1;
    char name[160] = "d:\\what000.bmp";
    while (count--)
    {
        ::BitBlt(hdcCompatible, 0, 0, w, h, hdc, 0, 0, SRCCOPY); 
        //BOOL b = ::PrintWindow(hwnd, hdcCompatible, 0);
        ::GetDIBits(hdcCompatible, hbm, 0, h, data, &infoHeader, DIB_RGB_COLORS);
        name[9] = (char)(20 - count + 'A');
        FILE * outfile = fopen(name, "wb");
        fwrite(&fileHeader, sizeof(fileHeader), 1, outfile);
        fwrite(&infoHeader.bmiHeader, sizeof(infoHeader.bmiHeader), 1, outfile);
        fwrite(data, 1, w*h * 3, outfile);
        fflush(outfile);
        fclose(outfile);
        Sleep(100);
    }

    ::DeleteObject(hbm);
    ::DeleteDC(hdcCompatible);
    ::ReleaseDC(hwnd, hdc);
    //delete []data;


    return 0;
}

