
# coding: utf-8

# In[1]:

#https://github.com/vivianLL/CatDogNames/blob/master/changeXML.py
import os
from xml.etree.ElementTree import parse, Element


# In[4]:

def batchRenameFile(DirName):
    
    FileList = os.listdir(DirName)
    for FileName in FileList:
        FilePath = DirName + '\\' + FileName
        #print(FilePath)
        doc = parse(FilePath)
        root = doc.getroot()
        sub1 = root.find("filename")
        name = sub1.text
        #print(name)
        sub2 = root.find("path")
        print(sub2.text)
        sub2.text = 'D:\Dataset\dataset\VOC_LPR\VOC2007\JPEGImages' +'\\'+ name + '.jpg'
        doc.write(FilePath)
        
if __name__ == '__main__':
    batchRenameFile('D:\Dataset\dataset\VOC_LPR\VOC2007\Annotations')


# In[ ]:


