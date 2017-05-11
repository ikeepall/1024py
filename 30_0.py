import os
all_files =os.listdir("C:\\Users\\Administrator\\Desktop")
print(all_files)
type=dict()

for f in all_files:
    if os.path.isdir(f):
        type.setdefault('文件夹',0)
        type_dict['文件夹']+=1
    else:
        ext = os.path.splitext(f)[1]
        type.setdefault(ext, 0)
        type[ext]+=1
for j in type.keys():
    print('该文件夹下共有共有类型为%s的文件%d个' %(j,type[j]) )

#2222

