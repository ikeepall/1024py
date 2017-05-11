f1=open("C:\\Users\\Administrator\\Desktop\\bbb.txt")
f2=open("C:\\Users\\Administrator\\Desktop\\xxx.txt")
count=0
fl1=f1.readlines()
fl2=f2.readlines()

for i in range(len(fl1) if len(fl1)>len(fl2) else len(fl2)):
    if fl1[i]!=fl2[i]:
        print("第%d行不一样" % i)
        count += 1
        l= len(fl1[i]) if len(fl1[i]) > len(fl2[i]) else len(fl2[i])
        for j in range(l):
            if fl1[i][j] != fl2[i][j]:
                print("第%d字符不一样" % j)
                break

print("一共%d处不一样" % i)
