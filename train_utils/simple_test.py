#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 14:47
# @Author  : zfl2_2wzy
# @Email  : 1822643111@qq.com
# @FileName: simple_test.py
# @Software: PyCharm

import torch
from my_dataset import PennFudanDatasets
from models import get_model_instance_segmentation, get_transform
from PIL import Image

dataset_test_real = PennFudanDatasets('PennFudanPed', get_transform(train=False))
torch.manual_seed(1)
indices = torch.randperm(len(dataset_test_real)).tolist()
dataset_test = torch.utils.data.Subset(dataset_test_real, indices[:])
# pick one image from the test set
img, _ = dataset_test[0]

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

num_classes = 2
# get the model using the helper function
model = get_model_instance_segmentation(num_classes)
# move model to the right device
model.to(device)

# put the model in evaluation mode
model.eval()
with torch.no_grad():
    prediction = model([img.to(device)])
    print(prediction)
    # info:输出信息
    # vis:可视化
    # Image.fromarray(img.mul(255).permute(1, 2, 0).byte().numpy())
    # Image.fromarray(prediction[0]['masks'][0, 0].mul(255).byte().cpu().numpy())
