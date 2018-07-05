##遍历指定path下所有文件，并将文件名d重命名为name
import os    
    
path = './Image'
for (root,dirs,files) in os.walk(path) :
    for item in files :
        Olddir = os.path.join(root, item)
        filename=os.path.split(Olddir)[0]   #文件名
        filetype=os.path.split(Olddir)[1][-4:]   #文件扩展名
        Newdir=os.path.join(path,str(count).zfill(6)+filetype)
        os.rename(Olddir, Newdir)
        count+=1