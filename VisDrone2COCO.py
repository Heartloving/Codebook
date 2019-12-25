# -*- encoding: utf-8 -*-
"""
@Author  : 凡
@Email   : Heartloving515@gmail.com
@File    : VisDrone2COCO.py`
@Time    : 2019/12/12 10:24
@Software: PyCharm
"""



import string
import os, sys
import glob
from PIL import Image
import json
import numpy as np
import cv2

'''
visdrone 标注格式: [bbox_top_left x	,bbox_top_left y,width,height,score,category,truncation,occlusion]
score:表示边界框的置信度，1表示可信，0表示不可信 （程序中把不可信box去除了）
category: ignored regions (0), pedestrian (1), people (2), bicycle (3), car (4), van (5), truck (6),
          tricycle (7), awning-tricycle (8), bus (9), motor (10), others (11))
truncation:截断，0： 无截断， 1：1%-50%截断
occlusion: 遮挡，无遮挡 0，部分遮挡 1，重遮挡 2'' 
'''

class  Converter:
	def __init__(self, path=None):
		# self.classes = ('__background__', 'boat', 'campingcar', 'car', 'others','pickup', 'plane', 'tractor',
        #                'truck', 'van') #VEDAI Dataset
		self.classes = ('__background__', 'pedestrian', 'person', 'car', 'van', 'bus', 'trunk', 'motor',
						'bicycle', 'awning-tricycle', 'tricycle')#VisDrone Dataset
		self.num_classes = len(self.classes)
		self.src_path = path
		self.annotaions_path = os.path.join(self.src_path, 'annotations')
		self.image_set_path = os.path.join(self.src_path, 'images')
		#self.categories_to_ids_map = self._get_categories_to_ids_map()
		#self.categories_msg = self._categories_msg_generator()

	def _get_img_lists(self):
		all_imgs = glob.glob(self.image_set_path + '/*.jpg')
		img_lists = []#图片名称列表
		for item in all_imgs:
			img_basename = os.path.basename(item) # 100.jpg
			temp1, temp2 = os.path.splitext(img_basename)#temp1:'100'  temp2: '.jpg'
			img_lists.append(temp1)
		return img_lists

	def _load_annotation(self, img_lists=[]):
		#ids = ids if _isArrayLike(ids) else [ids]
		image_msg = []#保存图片信息
		annotation_msg = []#保存标注信息
		annotation_id = 1
		ingore = 1
		for num,img in enumerate(img_lists):
			im = Image.open((self.image_set_path + '/' + img + '.jpg'))
			# print(num,img)
			width, height = im.size
			gt = open(self.annotaions_path + '/' + img + '.txt').read().splitlines()#获取txt文件中的gt box标注信息
			for img_each_label in gt:#对于每个box 标注信息
				ann = img_each_label.split(',')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为img_each_label.split(',')。
				#if int(ann[5]) == 11 or int(ann[5])==0:
					#print(ann)
				if int(ann[4]) == 0:#对于边界框不可信的不做考虑,如果不需要忽略，注释该段即可。
					ingore += 1
					continue

				one_ann_msg = {"segmentation":[[0]],
							   "image_id": int(num),#图片id
							   "iscrowd" : 0,
							   "ignore" :0,
							   "area": int(ann[2])*int(ann[3]),
							   "bbox": [int(ann[0]),int(ann[1]), int(ann[2]), int(ann[3])],#位置信息x,y,w,h
							   "category_id": int(ann[5]),#类别
							   "id": annotation_id,#bbox id
							   }
				annotation_msg.append(one_ann_msg)
				annotation_id += 1 #bbox id 加一


			one_image_msg = {"file_name": img + ".jpg",
							 "height": int(height),
							 "width": int(width),
							 "id": int(num)}
			image_msg.append(one_image_msg)

		#print('ignored bbox', ingore)
		print('saved bbox',annotation_id)
		print('picture num',num+1)

		return image_msg, annotation_msg


	def _save_json_file(self, filename=None, data=None):
		if not filename.endswith('.json'):
			filename += '.json'
		assert type(data) == type(dict()), 'data format {} not supported'.format(type(data))
		with open(filename, 'w') as f:
			f.write(json.dumps(data))



	def _categories_msg_generator(self):
		categories_msg = []
		for category in self.classes:
			if category == '__background__':
				continue
			one_categories_msg = {"supercategory":"none",
								  "id": dict(zip(self.classes,range(self.num_classes)))[category],
								  "name":category
								  }
			categories_msg.append(one_categories_msg)
		#print(categories_msg)
		return categories_msg


	def visdrone_to_coco(self):
		img_lists = self. _get_img_lists()
		img_msg, ann_msg = self._load_annotation(img_lists)
		result_json = {"images": img_msg,
					   "type": "instances",
					   "annotations": ann_msg,
					   "categories": self._categories_msg_generator()
					   }

		self._save_json_file('train', result_json)


if __name__ == '__main__':
	#路径是D:\\Education\\CODE\\jupter\\VisDrone2018 - DET - val\\images
	src_path = "../DataSets/VisDrone2019/VisDrone2018-DET-val"#linux 路径格式
	#src_path = "../DataSets/VisDrone2019/VisDrone2018-DET-train"  # linux 路径格式
	#src_path = "D:\\Education\\CODE\\jupter\\VisDrone2018-DET-val"#win 路径格式
	conver = Converter(src_path)
	conver.visdrone_to_coco()
