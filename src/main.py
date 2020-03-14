# -- coding: utf-8 --
from cuttingVideo import trancode_src_video_to_level5_and_cut_to_chunks
from trans_code_video import main as trans_code_chunk_to_other_level
from countVideoFileSizeInfo import plot_chunk_size_of_diffent_level

if __name__ == '__main__':
    trancode_src_video_to_level5_and_cut_to_chunks()
    trans_code_chunk_to_other_level()
    plot_chunk_size_of_diffent_level()