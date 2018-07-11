
# coding: utf-8

# In[20]:

import os
import random

imagefilepath='D:\Dataset\dataset\VOC_LPR\VOC2007\JPEGImages'
txtsavepath='D:\Dataset\dataset\VOC_LPR\VOC2007\ImageSets\Main\\'

trainval_percent=0.5 
train_percent=0.5

#get image name list
image_name_list = os.listdir(imagefilepath)
#shuffle
for i in range(3):
    random.shuffle(image_name_list)
#
num_examples = len(image_name_list)

trainval_test_split_point = int(num_examples*trainval_percent)
trainval = image_name_list[:trainval_test_split_point]
test = image_name_list[trainval_test_split_point:]

trainval_num_examples = len(trainval)
train_val_split_poin = int(trainval_num_examples*train_percent)
train = trainval[:train_val_split_poin]
val = trainval[train_val_split_poin:]

ftrainval = open(txtsavepath+'trainval.txt','w');  
ftest = open(txtsavepath+'test.txt','w');  
ftrain = open(txtsavepath+'train.txt','w');  
fval = open(txtsavepath+'val.txt','w')

for line in trainval:
    ftrainval.write(line[:-4]+'\n')
ftrainval.close()

for line in train:
    ftrain.write(line[:-4]+'\n')
ftrain.close()

for line in test:
    ftest.write(line[:-4]+'\n')
ftest.close()

for line in val:
    fval.write(line[:-4]+'\n')
fval.close()

print("Write Done!")


# In[ ]:




# In[ ]:



