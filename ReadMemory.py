import ctypes as c
from ctypes import wintypes as w
from msvcrt import kbhit
import os
import time
import psutil

#pid = 8712  # NES EMULATOR FCEUX pid
pid = 0

for Process in psutil.process_iter(): #look for pid of process name
	#print(Process.name())
	if Process.name() == "fceux.exe":
		pid = Process.pid
		print("pid is:"+str(pid))
time.sleep(3)

#aki sta lo k mola
k32 = c.windll.kernel32
OpenProcess = k32.OpenProcess
ReadProcessMemory = k32.ReadProcessMemory
WriteProcessMemory = k32.WriteProcessMemory
GetLastError = k32.GetLastError
CloseHandle = k32.CloseHandle

processHandle = OpenProcess(0x1F0FFF, False, pid) #nos acoplamos al processo con todos los permisos y sacamos su handle
print (processHandle)  #all your base are belonge tu us

addr = 0x0000000002591862  # addres of coins for smw3  (busco con cheatengine)
ReadBuffer = c.c_uint()
value=100    #lo k vamos a enviar 100 COINS for u MARIO
WriteBuffer = c.c_uint(value) 

while True:
	os.system('cls' if os.name == 'nt' else 'clear') #clear screen
	result = ReadProcessMemory(processHandle, addr, c.byref(ReadBuffer), c.sizeof(ReadBuffer), c.c_ulong(0))  #read data
	e = GetLastError()
	print('result: {}, err code: {}, bytesRead: {}'.format(result,e, c.sizeof(ReadBuffer)))
	print('data: {:016X}h'.format(ReadBuffer.value))
	if kbhit():  #if key hit write and exit loop
		result = WriteProcessMemory(processHandle, addr, c.byref(WriteBuffer), c.sizeof(WriteBuffer), c.c_ulong(0)) #write data
		e = GetLastError()
		print('result: {}, err code: {}, bytesSent: {}'.format(result,e,c.sizeof(WriteBuffer)))
		print('data: {:016X}h'.format(WriteBuffer.value))
		print("1UP!! por k tu molas")
		break
	time.sleep(0.1)
CloseHandle(processHandle)