# _*_ coding: utf-8 _*_
import os
from PIL import Image
from ffmpy import FFmpeg

in_img_path = './runlang'
out_img_path = './runlang'

pic_list = os.listdir(in_img_path)
for pic in pic_list:
    pic_name = pic.split('.')[0]
    pic_path = os.path.join(in_img_path, pic) 
    img = Image.open(pic_path)
    in_w, in_h = img.size
    out_w = in_w
    out_h = in_h
    size = '{}x{}'.format(out_w, out_h)
    out_name = out_img_path + '/' + pic_name + '_' + size + '.yuv'
    
    ff = FFmpeg(inputs={pic_path:None}, outputs = {out_name:'-s {} -pix_fmt nv21'.format(size)})
    print 'ff.cmd'
    ff.run()
