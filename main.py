import os
shutdown=input('Do you wish to shutdown? YES/NO')
if shutdown=='no':
   exit()
else:
 os.system('shutdown /s /t 0')

