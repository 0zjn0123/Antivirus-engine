by zjn|小逮逮|0zjn0123|https://github.com/0zjn0123/
import os
def cc(lj, zzwjj_ml):
    for path, dirnames, filenames in os.walk(lj):
        # print("路径：" + path + "包含文件夹：" + str(dirnames) + "包含文件：" + str(filenames))
        if str(dirnames) or str(filenames) == zzwjj_ml:
            return {'lj':path,'wjj':dirnames,'wj':filenames}
