# Mask R-CNN 

## 环境配置
* python3
* pytorch：>= 1.5
* pycocotools(Linux: pip install pycocotools;   
  Windows下的详细建议按照该[方法](https://www.cnblogs.com/masbay/p/10727280.html) 安装.
  强烈推荐安装[anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/) 的同时安装[Visual Studio](https://visualstudio.microsoft.com/zh-hans/vs/) 。
  毕竟深度学习的代码底层使用的是.cpp .h等，需要进行必要且必要的编译
* Ubuntu或Centos(不建议Windows)
* 最好使用GPU训练

## 文件结构
* ├──── coco_eval:来源于PyTorch官方的references/detection/，一些封装好的用于模型训练和测试的函数
* ├──── coco_utils:来源于PyTorch官方的references/detection/，一些封装好的用于模型训练和测试的函数
* ├── train_utils、utils: 训练验证相关模块
* ├── my_dataset.py: 自定义dataset用于读取PennFudanDataset数据集
* ├── train.py: 以MobileNetV2做为backbone进行训练
* ├── module.py: 定义MobileNetV2的模型构建
* ├── engine.py: 来源于PyTorch官方的references/detection/，一些封装好的用于模型训练和测试的函数

## 数据集
* 本教程使用Penn-Fudan的行人检测和分割数据集来训练Mask R-CNN实例分割模型。Penn-Fudan数据集中有170张图像，包含345个行人的实例。图像中场景主要是校园和城市街景，每张图中至少有一个行人，可看链接[PennFudanDataset数据集](https://www.cis.upenn.edu/~jshi/ped_html/)
* 也可以直接下载
    * wget https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip 
    * unzip PennFudanPed.zip


## 实验前准备
* 先理好自己的实验目的，到底是分类、分割还是目标检测等等；
* 理清实验目的，再去找相应方法(网络)的代码；
* 实现同一demo时候使用的深度学习框架诸多，如 [tensorflow](https://tensorflow.google.cn/) [keras](https://keras.io/) [pytorch](https://pytorch.org/) [mxnet](https://mxnet.apache.org/versions/1.7.0/) [paddlepaddle](https://www.paddlepaddle.org.cn/) [lua](http://www.lua.org/) [Jupyter Notebook](https://jupyter.org/) 
  目前这些列举的都是脚本类的框架(python lua等)，更别说Java、C++、cuda、matlab、shell等“兄弟”了（Java、C++、cuda、matlab、shell： 谁和TM是兄弟，是兄dier！！）。总结一句：深度学习，NB
* 下载代码时注意阅读readme.md里的内容！版本不正确，程序起不来；升级不谨慎，代码全靠改 ~~~ 5555 ~~~
* 准备数据集，建议使用readme.md指定的“官方”数据集。如若未指定，请自觉下载对应公开数据集首先测试demo可用性，再者可按照公开数据集格式只做自己的数据集，更有甚者可直接将图片、文字、音频、表格放入对应目录即可；
* demo可用性测试完建议开始制备自己的数据集；
* 训练自己的数据时候注意在代码中修改对应的数据集路径
    * train.py 代码中的23 24行

## 深层研究
* 由于该demo使用的是torchvision自带的特征提取模块(maskrcnn_resnet50_fpn:backbone + neck),预训练权重是默认的；
    * model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
    * 修改模型的backbone + neck可采用两种方案：<1>、替换掉模型的骨干网络。举例来说，默认的骨干网络（ResNet-50）对于某些应用来说可能参数过多不易部署，可以考虑将其替换成更轻量的网络（如MobileNet）<2>、仿照torchvision重新书写backbone和neck，如backbone修改成CSPDarkNet53,neck改成BiFPN等
    * 采用预训练的模型，在修改网络最后一层后finetune
* 由于该demo使用的测试网络极其简单，大家使用的时候请修改
* 运行代码的同时，重复研读论文会让你豁然开朗。

## 参考
* 链接1 [pytorch](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)
* 链接2 [博客](https://blog.csdn.net/u013685264/article/details/100564660 )
* 链接3 [Mask R-CNN paper](http://cn.arxiv.org/pdf/1703.06870v3) [Mask R-CNN demo](https://github.com/jytime/Mask_RCNN_Pytorch)
* 链接4 [Faster R-CNN paper](https://arxiv.org/abs/1506.01497) [Faster R-CNN demo](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/master/pytorch_object_detection/faster_rcnn) [理论讲解 视频序列](https://www.bilibili.com/video/BV1af4y1m7iL)

## 谢谢各位
~~~ 谢谢你们， 感谢遇见 ~~~，