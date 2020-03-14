# coding:utf-8

import csv
import os
import subprocess
import time
from Chunk_quality_level_enum import *


def trans_chunks_code_to_low_level(input_dir, current_level):
    '''
    将一个文件夹中的所有chunks转码到比当前level低的各个level中，并统计时间
    :param input_dir: 要转码的chunks所在的文件夹
    :param current_level: 当前的level
    :return:
    '''
    create_record_csv = open("../video/level %s to lower level.csv" % current_level, "w",newline='')
    csv_write = csv.writer(create_record_csv)
    headers = ["des level", "start_time", "end_time", "time（s）"]
    csv_write.writerow(headers)
    for i in range(current_level - 1, 0, -1):
        out_dir = input_dir+"/level%s"%i
        make_dirs_if_not_exists(out_dir)
        start_time = time.time()
        transcode_from_levlm_to_leveln(src_dir=input_dir,level_m=current_level,level_n=i,out_dir=out_dir)
        end_time = time.time()
        csv_write.writerow([i,start_time,end_time,end_time-start_time])

    create_record_csv.close()

def transcode_from_levlm_to_leveln(src_dir,level_m,level_n,out_dir):
    '''
    扫描src_dir下面的所有文件，并转码到level n
    :param src_dir:
    :param level_m:
    :param level_n:
    :return:
    '''
    rate = get_bit_rate_by_level(level_n)
    width = get_width_by_level(level_n)
    height = get_height_by_level(level_n)
    for root,dirs,files in os.walk(src_dir):
        for file in files:
            cmd = "ffmpeg -y -i %s -s %sx%s -b:v %sk -acodec copy %s" % (src_dir+'/'+file, width, height, rate, out_dir+'/'+file)
            run_command(cmd)


def make_dirs_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def move_dir_override_if_exist(src_dir,des_dir):
    pass

def trans_video_code(input_file, width, height, rate, out_file):
    '''
    将一个视频文件转码并更改分辨率到out_file
    :param input_file: 原视频路径
    :param width:  目标视频分辨率
    :param height: 目标视频分辨率
    :param rate: 比特率
    :param out_file:
    :return:
    '''

    cmd = "ffmpeg -y -i %s -s %sx%s -b:v %sk -acodec copy %s" % (input_file, width, height, rate, out_file)
    return run_command(cmd)


def cutting_video_to_chunks(input_file, chunk_size, level):
    '''
    将完整的视频，切成每个时长是是多少秒的
    :param input_file:
    :param chunk_size: 每个chunk的秒数
    :param level 1~5
    :return:
    '''
    dir = "../video/level%s" % level
    os.mkdir(dir)
    for left in range(0, 596, chunk_size):
        out_file = "%s/%s-%s.avi" % (dir, left, left + chunk_size)
        cmd = "ffmpeg -y -i %s -ss %s -t %s -acodec copy -vcodec copy %s" % (input_file, left, chunk_size, out_file)
        res = run_command(cmd)
        if not res:
            break


def run_command(cmd):
    try:
        res = subprocess.call(cmd, shell=True)
        if res != 0:
            return False
        return True
    except Exception:
        return False
