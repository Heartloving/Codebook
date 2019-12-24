# -*- encoding: utf-8 -*-
"""
@Author  : 凡
@Email   : Heartloving515@gmail.com
@File    : video2frame.py
@Time    : 2019/12/24 11:30
@Software: PyCharm
"""

import os
import cv2
from tqdm import tqdm
def video2frame(video_src_path, frame_save_path):
    videos = os.listdir(video_src_path)
    print(videos)
    for video in videos:
        print("正在读取视频：", video)
        video_name = video[:-4]
        if video_name not in os.listdir(frame_save_path):
            os.mkdir(frame_save_path + video_name)
            print("正在创建'%s'文件夹" % video_name)
        save_path = os.path.join(frame_save_path, video_name) + "/"
        video_path = os.path.join(video_src_path, video)
        cap = cv2.VideoCapture(video_path)
        #cap = cv2.VideoCapture(0)，参数0似乎可以打开电脑摄像头，参数是视频文件路径则打开视频
        if cap.isOpened():
            success = True
            print("读取成功!")
        else:
            success = False
            print("读取失败!")
        totalFrameNumber = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(totalFrameNumber)
        #frame_count = 0
        for i in tqdm(range(totalFrameNumber)):
        #while (success):
            success, frame = cap.read()
            if i % 3 ==0:  #帧间隔
                # print("---> 正在保存第%d帧:" % frame_count, success)
                # resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)#如果需要固定尺寸帧，可以resize
                # cv2.imwrite(save_path + "%d.jpg" % frame_count, resize_frame)
                cv2.imwrite(save_path + "%d.jpg" % i, frame)
                # frame_count += 1

    cap.release()
if __name__ == '__main__':
    videos_src_path = "videos/"#视频读取文件夹
    frames_save_path = "frames/"#帧保存文件夹
    video2frame(videos_src_path, frames_save_path)
