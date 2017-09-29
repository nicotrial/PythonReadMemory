import ctypes as c
from ctypes import wintypes as w
from msvcrt import kbhit
import os
import time

pid = 1864  # explorer pid

k32 = c.windll.kernel32

OpenProcess = k32.OpenProcess
OpenProcess.argtypes = [w.DWORD,w.BOOL,w.DWORD]
OpenProcess.restype = w.HANDLE

ReadProcessMemory = k32.ReadProcessMemory
ReadProcessMemory.argtypes = [w.HANDLE,w.LPCVOID,w.LPVOID,c.c_size_t,c.POINTER(c.c_size_t)]
ReadProcessMemory.restype = w.BOOL

GetLastError = k32.GetLastError
GetLastError.argtypes = None
GetLastError.restype = w.DWORD

CloseHandle = k32.CloseHandle
CloseHandle.argtypes = [w.HANDLE]
CloseHandle.restype = w.BOOL

processHandle = OpenProcess(0x10, False, pid)
print (processHandle)


data = c.c_ulong()
bytesRead = c.c_ulonglong()

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	if kbhit():
		break
	addr = 0x000000000330F938  # addres of mouse X in explorer.exe
	result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
	e = GetLastError()

	print('result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
	print('data: {:016X}h'.format(data.value))

	addr = 0x000000000330F934  # addres of mouse X in explorer.exe
	result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
	e = GetLastError()

	print('result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
	print('data: {:016X}h'.format(data.value))
	time.sleep(0.01)
CloseHandle(processHandle)