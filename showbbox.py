from pycocotools.coco import COCO
import cv2
import os, sys
import glob
import string



def show_anns(annFile, imageFile, resultFile):
    """
    函数功能：读取图片数量，并对每一张图片进行标注并讲结果保存到resultFile文件夹中。
    :param annFile:使用的标注文件
    :param imageFile:要读取的image所在文件夹
    :param resultFile:画了标注之后的image存储文件夹
    :return:
    """
    classes = ('__background__', 'pedestrian', 'person', 'car', 'van', 'bus', 'trunk', 'motor',
               'bicycle', 'awning-tricycle', 'tricycle')  # VisDrone Dataset
    all_imgs = glob.glob(imageFile + '/*.jpg')
    print(len(all_imgs))
    #     img_lists = []

    coco = COCO(annFile)
    #for img_id in range(len(all_imgs)):
    for img_id in range(500):
        img = coco.loadImgs(img_id)
        #print(img[0])
        image = cv2.imread(os.path.join(imageFile, img[0]['file_name']))
        print(image)


        annIds = coco.getAnnIds(imgIds=img_id, iscrowd=None)
        anns = coco.loadAnns(annIds)
        #print(anns)
        for n in range(len(anns)):
            x, y, w, h = anns[n]['bbox']
            x, y, w, h = int(x), int(y), int(w), int(h)
            #print(x, y, w, h)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))

            cv2.putText(image,classes[anns[n]['category_id']], (x, y),
                        cv2.FONT_HERSHEY_PLAIN, 1.0, ( 255, 0, 0), 1)#显示类别标注信息
            #cv2.putText(image,str(anns[n]['bbox']), (x, y + h),
            #            cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 0), 1)#显示bbox坐标信息

        if not os.path.exists(resultFile):
            os.makedirs(resultFile)
        #保存文件时必须要先新建文件夹,如果不新建文件夹会无法保存图片，而且不会报错提示
        #print(resultFile +'result'+ img[0]['file_name'])
        cv2.imwrite(resultFile +'result'+ img[0]['file_name'], image)
        #cv2.imwrite(os.path.join(resultFile, img[0]['file_name']), image)

    print("生成图片存在{}".format(resultFile))

if __name__ == "__main__":
    root_path = '/media/xddz/本地磁盘/Learning/CODE_DATA/DATA/VisDrone/'
    annFile = root_path + 'annotations/instances_test.json'
    imageFile = root_path + 'test/'
    resultFile = root_path + 'result_test/'
    show_anns(annFile, imageFile, resultFile)

# ————————————————
# 版权声明：本文为CSDN博主「学_生(学习)」的原创文章，遵循 CC 4.0 BY 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/zhuoyuezai/article/details/84315113
# ————————————————
