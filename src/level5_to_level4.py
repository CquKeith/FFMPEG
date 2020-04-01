# -- coding: utf-8 --
# test level5 transcode to level4

from countVideoFileSizeInfo import statics_chunks_info
from cuttingVideo import trancode_src_video_to_level5_and_cut_to_chunks
from main import remove_old_dir

# src to level 1
# ffmpeg -y -i ../../1080p_24fps/big_buck_bunny_1080p_surround.avi -c:v libx264 -x264-params "nal-hrd=cbr:f
# orce-cfr=1" -b:v 500K -minrate 500K -maxrate 500K  ../video/level1.ts
# size

def main():
    remove_old_dir()
    trancode_src_video_to_level5_and_cut_to_chunks()
    statics_chunks_info('../video/level5')

if __name__ == '__main__':
    main()
