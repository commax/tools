# _*_ coding: utf-8 _*_
import os
from PIL import Image
from ffmpy import FFmpeg

video_path = './origin.avi'
#jpeg_path = os.mkdir('./jpegs')
#yuv_path = os.mkdir('./yuvs')
jpeg_path = './jpegs'
yuv_path = './yuvs'

if os.path.isdir(jpeg_path)
    os.mkdir(jpeg_path)
if not os.path.isdir(yuv_path)
    os.mkdir(yuv_path)

jpeg_name = os.path.join(jpeg_path. '/img%d.jpeg')

ff = FFmpeg(inputs={video_path:None}, outputs={jpeg_name: '-r 25'})
print 'ff.cmd'
ff.run()

pic_list = os.listdir(jpeg_path)
for pic in pic_list:
    pic_name = pic.split('.')[0]
    pic_path = os.path.join(jpeg_path, pic) 
    img = Image.open(pic_path)
    in_w, in_h = img.size
    out_w = in_w
    out_h = in_h
    size = '{}x{}'.format(out_w, out_h)
    yuv_name = yuv_path + '/' + pic_name + '_' + size + '.yuv'
    
    ff = FFmpeg(inputs={pic_path:None}, outputs = {yuv_name:'-s {} -pix_fmt nv21'.format(size)})
    print 'ff.cmd'
    ff.run()
