import os
if os.path.exists('C:\Lab 6\ dir'):
    for i in os.listdir():
        os.remove('C:\Lab 6\ dir')
else:
    print("no such file")