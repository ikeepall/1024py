import os
file_name="xxx.txt"
dir="C:\\"
temp=list(os.walk(dir))
for each in temp:
    x=str(each)
    if x.find(file_name)!=-1:
        print (each[0]+"\\"+file_name)