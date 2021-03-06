# -- coding: utf-8 --
import os
import shutil

from captureImage import main as captureImage
from countVideoFileSizeInfo import plot_chunk_size_of_diffent_level
from cuttingVideo import trancode_src_video_to_level5_and_cut_to_chunks
from trans_code_video import main as trans_code_chunk_to_other_level


def remove_dir_if_exist(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def remove_old_dir():
    for level in range(1, 6):
        remove_dir_if_exist('../video/level%s' % level)


if __name__ == '__main__':
    remove_old_dir()
    trancode_src_video_to_level5_and_cut_to_chunks()
    trans_code_chunk_to_other_level()
    plot_chunk_size_of_diffent_level()
    captureImage()
