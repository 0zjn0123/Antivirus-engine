import os
for i in range(20):
    s = r"D:\病毒" + os.sep + str(i)
    os.makedirs(s)
    s = r"D:\病毒" + os.sep + str(i) + os.sep + "aaa.py"
    e = open(s,'w')
