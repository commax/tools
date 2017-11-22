import os
filedir=os.getcwd()+'/merge2'
filelist=os.listdir(filedir)
for item in filelist:
    print item

mergefile=open('merge2/merge.yuv','w')
for item in filelist:
    filepath=filedir+'/'+item
    for yuv in open(filepath,'r'):
        mergefile.write(yuv)
mergefile.close()
