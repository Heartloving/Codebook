from pycocotools.coco import COCO
import numpy as np
import cv2
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='/home/wenxiangyu/showvis'
#'/home/wenxiangyu/Dataset/VEDAI9'
dataType='val2017'
annFile='/home/wenxiangyu/showvis/annotations/instances_val2017.json'
# 初始化标注数据的 COCO api
coco=COCO(annFile)

# cats = coco.loadCats(coco.getCatIds())
# nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))
#
# nms = set([cat['supercategory'] for cat in cats])
# print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['car']);
#imgIds = coco.getImgIds(catIds=catIds );

imgIds = coco.getImgIds(imgIds = [3])
#print(imgIds)
# loadImgs() 返回的是只有一个元素的列表, 使用[0]来访问这个元素
# 列表中的这个元素又是字典类型, 关键字有: ["license", "file_name",
# "coco_url", "height", "width", "date_captured", "id"]
img = coco.loadImgs(imgIds)[0]
print(img)
# 加载并显示图片,可以使用两种方式: 1) 加载本地图片, 2) 在线加载远程图片
# 1) 使用本地路径, 对应关键字 "file_name"
#file_name="00000010.png"
#I = io.imread('%s/%s/%s'%(dataDir,dataType,file_name))
I = io.imread('%s/%s/%s'%(dataDir,dataType,img['file_name']))
# 2) 使用 url, 对应关键字 "coco_url"
#I = io.imread(img['coco_url'])
# plt.axis('off')
# plt.imshow(I)
# plt.show()

# 加载并显示标注信息
plt.imshow(I)
#plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
print(anns)
coco.showAnns(anns)
resultFile = '/home/wenxiangyu/Dataset/VEDAI9/annotations/result/'
img1 = cv2.imread(r"/home/wenxiangyu/Dataset/VEDAI9/images/test1122/00000025.png")
print(img1)
for n in range(len(anns)):
    x, y, w, h = anns[n]['bbox']
    x, y, w, h = int(x), int(y), int(w), int(h)
    print(x, y, w, h)

    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0))
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255),2)
cv2.imwrite('/home/wenxiangyu/Dataset/VEDAI9/images/result/result.png',img1)
    # print("生成图片存在{}".format(resultFile))

#plt.show()

