# Energy and Carbon Emissions of Modern Video Encoders
In this project, we provide a comparative study between five leading video coding standards, namely H.264/AVC, H.265/HEVC, H.266/VVC, VP9, and AV1 through their open-source and fast software encoders x264, x265, VVenC, libvpx-vp9, and SVT-AV1, respectively, in terms of quality, energy consumption, CO2 emissions and CPU and memory usage. This study provides a better understanding of the trade-off between energy consumption, bitrate, and quality of different encoders and determines which is the most suitable for developing a green and sustainable video streaming solution.

For further information about the project, you can find additional details from [here](https://chachoutaieb.github.io/encoding_energy_co2).

## Install 


```bash
git clone https://github.com/chachoutaieb/encoding_energy_co2.git
pip3 install -r requirements.txt

```
- [Install VVenC](https://github.com/fraunhoferhhi/vvenc/)
- [Install VVdeC](https://github.com/fraunhoferhhi/vvdec)
- Install ffmpeg 5



## Download Dataset

- [x] [Original dataset](https://jvet.hhi.fraunhofer.de/)
- [x] The whole encoded dataset can be shared upon request. Please, send an email to taieb.chachou[at]gmail.com with Cc sfezza[at]ensttic.dz and Wassim.Hamidouche[at]insa-rennes.fr.

Note : make all the downloaded dataset in the dataset directory

## Usage

- To encode JVET-CTC dataset used in our project with the target encoding parameter defined in data/bitrate-final.xlsx and with estimation of the energy , co2 emissions, CPU or GPU usage, etc. we use the following command:

```bash


python3 '/your-path-to-the-project/encoding_energy_co2.py' \
      -d '/your-path-to-the-project/original_dataset' \
      -r '/your-path-to-the-project/encoding_results.xlsx' \
      -p platform type (CPU or GPU) \
      -sp preset type (CPU : veryslow, medium, fast, faster | GPU : slow, medium, fast) \
      -m psnr ssim vmaf  
      
```

- To encode your own video with estimation of the energy, co2 emissions, CPU or GPU usage, etc. we use the following command:

```bash
python3 '/your-path-to-the-project/encoding_energy_co2.py' \
      -i '/your-path-to-the-project/inputVideo.yuv (.yuv, .y4m, .mp4, etc.)' \
      -o '/your-path-to-the-project/outputVideo.mp4 (.mp4, .266, .265, etc.)' \
      -r '/your-path-to-the-project/encoding_results.xlsx' \
      -s resolution ('WxH') \
      -f framerate (fps) \
      -x bit depth (8 or 10) \
      -b Bitrate (kb/s) \
      -c codec (x264, x265, vp9, svt-av1, vvenc) \
      -p Platform type (CPU or GPU) \
      -sp preset type (CPU : veryslow, medium, fast, faster | GPU : slow, medium, fast) \
      -m psnr ssim vmaf
```    
  
  
***Note : On the GPU platform, the max bit depth for x264 is 8-bit. For this purpose all video with 10-bit are encoded automatically with a pixel format of 8-bit for this codec. You can find more information about that [here](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new).



```bash

# you will see

red : Raw video does not exist 
green : Encoded video is ready
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|                       Encoded video                        | Time (s) |Bitrate(kb/s)| Energy (Wh)  |  CO2eq (g)  |  PSNR  |  SSIM  |  VMAF  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|           ArenaOfValor_1920x1080_60_8bit_420.yuv           |                          The raw video does not exist                          |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_3200k_50fps_libx264_faster.mp4     |  0.647   |    3332     | 0.0005615727 | 0.000056719 | 33.86  |  0.88  | 86.41  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_2200k_50fps_libx264_faster.mp4     |  0.583   |    2326     | 0.0005136440 | 0.000051878 | 32.36  |  0.86  | 78.85  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_1200k_50fps_libx264_faster.mp4     |  0.548   |    1299     | 0.0004840514 | 0.000048889 | 30.04  |  0.81  | 63.67  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_750k_50fps_libx264_faster.mp4      |  0.501   |     818     | 0.0004485373 | 0.000045302 | 28.20  |  0.77  | 50.48  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_1020k_50fps_libx265_faster.mp4     |  5.422   |    1105     | 0.0043473697 | 0.000439084 | 32.89  |  0.88  | 78.70  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|     BasketballDrillText_800k_50fps_libx265_faster.mp4      |  4.751   |     871     | 0.0038191997 | 0.000385739 | 32.05  |  0.86  | 73.25  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+


```


## Results

#### The results of this project can be found on the following [website](https://chachoutaieb.github.io/encoding_energy_co2).


