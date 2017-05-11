import os
all_files =os.listdir(os.curdir)
os.chdir(os.curdir)
for f in all_files:
    print("%s的大小是%d" % (f,os.path.getsize(f)))
    # print(os.path.getsize(os.curdir+"/"+f))