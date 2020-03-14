# -- coding: utf-8 --
# cutting src video file to chunks, and then statics duration,size,bitrate of each chunk

from cuttingVideo import cut_source_video_to_chunks
from countVideoFileSizeInfo import statics_chunks_info


if __name__ == '__main__':
    # cut_source_video_to_chunks()
    statics_chunks_info('../video/levelsrc')