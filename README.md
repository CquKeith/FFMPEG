# 实验步骤
1. 将原视频转成level5的视频 level5.avi
2. 将level5.avi切成大小是2s的chunk
3. 将level5的chunks依此转成level 4~1的chunks，并统计时间
4. 依次将level4的chunks依次转化成level 3~1，并统计转码时间
5. 直到level 2的chunks全部转化成level 1，并统计转码时间

6. 统计level5，和level5转成level 4~1的各chunk的大小的平均值，方差，协方差

7. 挑选整片第120s处的视频，通过ffmpeg截图出来，并拼接到一个visio中。

# 结果整理

### 实验条件

- ffmpeg 
  - Version： 4.2.2
  - available：http://ffmpeg.org
- video source
  - available：http://www.bigbuckbunny.org
  - big_buck_bunny_1080p_surround 24fps
- windows（in VM fusion）
  - version：win10 64bits
  - CPU：Intel(R) Core(TM) i5-5257U CPU@2.7Hz @2.7Hz
  - memory：2G
  - python：
    - version：Python 3.8.1
- chunk
  - duration : 2s

### 视频质量

| quality level | bitrate(bps) | resolution |
| :-----------: | :----------: | :--------: |
|       5       |     100K     |  192*144   |
|       4       |     300K     |  320*240   |
|       3       |     600K     |  480*360   |
|       2       |     900K     |  640*480   |
|       1       |    1500K     |  1280*720  |

### 转码时间

| src level | des level | avg time(ms) |
| :-------: | :-------: | :----------: |
|     5     |     4     |    273.6     |
|     5     |     3     |    402.1     |
|     5     |     2     |    389.9     |
|     5     |     1     |    413.7     |
|     4     |     3     |    180.3     |
|     4     |     2     |    210.8     |
|     4     |     1     |    316.0     |
|     3     |     2     |    180.6     |
|     3     |     1     |    286.5     |
|     2     |     1     |    137.9     |

### chunk size

level 5是由1080p 24fps的源文件转码分割而来

level1～4是由level5转码而来

| level | avg size（KB）(level5 - level k,k=4,3,2,1) | variance | covariance |
| :---: | :----------------------------------------: | :------: | :--------: |
|   1   |                   176.7                    |  129.1   |   129.5    |
|   2   |                   258.3                    |  882.4   |   885.4    |
|   3   |                   371.8                    |  2969.6  |   2979.6   |
|   4   |                   481.0                    |  6116.3  |   6136.9   |
|   5   |                   459.4                    |  7297.6  |   7322.1   |

![image-20200309175819972](/Users/chenmengliang/Library/Application Support/typora-user-images/image-20200309175819972.png)