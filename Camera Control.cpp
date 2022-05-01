#include <windows.h>

char* linkChar=\"[http://172.31.0.66/ajaxcom?szCmd={\"SysCtrl\":{\"PtzCtrl\":{\"nChanel\":0,\"szPtzCmd\":\"right_start\",\"byValue\":50}}}]\"

ShellExecute(NULL, NULL, linkChar, NULL, NULL, SW_SHOWNORMAL);