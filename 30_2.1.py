import os
target="xxx.txt"
start_dir="C:\\"
def search_file(start_dir,target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd()+os.sep+each_file)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)
search_file(start_dir,target)