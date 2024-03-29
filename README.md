# Energy Consumption and Carbon Emissions of Modern Software Video Encoders
In this project, we provide a comparative study between five leading video coding standards, namely H.264/AVC, H.265/HEVC, H.266/VVC, VP9, and AV1 through their open-source and fast software encoders x264, x265, VVenC, libvpx-vp9, and SVT-AV1, respectively, in terms of energy consumption, CO2 emissions and coding efficiency. This study provides a better understanding of the trade-off between energy consumption, bitrate, and quality of different encoders and determines which is the most suitable for developing a green and sustainable video streaming solution.

For more information on the project, you can find additional details [here](https://chachoutaieb.github.io/encoding_energy_co2).

## Install 

- [Install VVenC](https://github.com/fraunhoferhhi/vvenc/)
- [Install VVdeC](https://github.com/fraunhoferhhi/vvdec)
- Install ffmpeg (version >= 5.2)
- [Install CodeCarbon](https://github.com/mlco2/codecarbon) (version 2.3.1) 

```bash
git clone https://github.com/chachoutaieb/encoding_energy_co2.git
pip3 install -r requirements.txt
sudo chmod a=r /sys/class/powercap/intel-rapl:0/energy_uj

```



## Download Dataset

- [x] [Original dataset](https://jvet.hhi.fraunhofer.de/)
- [x] The whole encoded dataset can be shared upon request. Please, send an email to taieb.chachou[at]gmail.com with Cc sfezza[at]ensttic.dz and Wassim.Hamidouche[at]insa-rennes.fr.

Note : make all the downloaded dataset in the dataset directory

## Usage

- To encode JVET-CTC dataset used in our project with the target encoding parameter defined in data/bitrate-final.xlsx, in order to estimate the energy , CO2 emissions, CPU or GPU usage, etc. You can use the following command:

```bash


python3 '/your-path-to-the-project/encoding_energy_co2.py' \
      -d '/your-path-to-the-project/original_dataset' \
      -r '/your-path-to-the-project/encoding_results.xlsx' \
      -p platform type (CPU or GPU) \
      -sp preset type (CPU : 'slower', 'medium', 'fast', 'faster' | GPU : 'slow', 'medium', 'fast') \
      -it Energy interval period in seconds. (optional) \
      -m 'psnr' 'ssim' 'vmaf'
      
``` 
  
  
***Note : On the GPU platform, the max bit depth for h264_nvenc is 8-bit. For this purpose, all videos with 10-bit are encoded automatically with a pixel format of 8-bit for this codec. You can find more information about that [here](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new).



```bash

# you will see the following result

The energy value is calculated with the following interval period: x264 = 0.3s, x265 = 0.5s, vp9 = 2.0s, VVenC = 3.0s, SVT-AV1 = 0.5s.
 You can change them according to the performance of machine by using the "-it" option.

red : Raw video does not exist 
green : Encoded video is ready
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|                       Encoded video                        | Time (s) |Bitrate(kb/s)| Energy (Wh)  |  CO2eq (g)  |  PSNR  |  SSIM  |  VMAF  |
+------------------------------------------------------------+----------+-------------+--------------+-------------+--------+--------+--------+
|           ArenaOfValor_1920x1080_60_8bit_420.yuv           |                        Error: The raw video does not exist                     |
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
## Citation

We kindly ask you to cite our paper if you find the repository useful to your work:

```bibtex
@article{chachou2023energyenc,
  title={Energy Consumption and Carbon Emissions of Modern Software Video Encoders},
  author={Chachou, Taieb and Hamidouche, Wassim and Fezza, Sid Ahmed and Belalem, Ghalem},
  journal={IEEE Consumer Electronics Magazine},
  year={2023},
  publisher={IEEE}
}
```

## Results

#### The results of this project can be found on the following [website](https://chachoutaieb.github.io/encoding_energy_co2).


