# Energy Consumption and Carbon Emissions of Modern Video Encoders
In this project, we provide a comparative study between five leading video coding standards, namely H.264/AVC, H.265/HEVC, H.266/VVC, VP9, and AV1 through their open-source and fast software encoders x264, x265, VVenC, libvpx-vp9, and SVT-AV1, respectively, in terms of quality, energy consumption and CO2 emissions. This study provides a better understanding of the trade-off between energy consumption, bitrate, and quality of different encoders and determines which is the most suitable for developing a green and sustainable video streaming solution.

## Install 


```bash
git clone https://github.com/chachoutaieb/encoding_energy_co2.git
pip3 install -r requirements.txt

```

## Download Dataset

- [x] [Original dataset](https://jvet.hhi.fraunhofer.de/)
- [x] The whole encoded dataset can be shared upon request. Please, send an email to taieb.chachou[at]gmail.com with Cc sfezza[at]ensttic.dz.

Note : make all the downloaded dataset in the dataset directory

## Usage

```bash

python3 /your-path-to-the-project/encoding_video.py
-s /your-path-to-the-project/original_dataset \
-t '/your-path-to-the-project/encoding_results.xlsx' \
-v 'CPU' -m psnr ssim vmaf

```
## Results

### Encoding performance (Energy, CO2 emissions, Encoding time, CPU and memory usage)



  Energy and CO2 emissions     |  CPU and memory usage         |  Encoding time                | 
:-----------------------------:|:-----------------------------:|:-----------------------------:
 ![](figures/Bar_dataset.jpg)  | ![](figures/bar_cpu_memory_time.jpg)  |  ![](figures/line_dataset_time.jpg)   


 
 ### Quality
 
 
 
   PSNR     |  SSIM         |  VMAF                | 
:-----------------------------:|:-----------------------------:|:-----------------------------:
 ![](figures/line_dataset_PSNR.jpg)  | ![](figures/line_dataset_SSIM.jpg)  |  ![](figures/line_dataset_VMAF.jpg)  
 ![](figures/dataset_BD_rate_(PSNR)_relative_Energy.jpg)  | ![](figures/dataset_BD_rate_(SSIM)_relative_Energy.jpg)  |  ![](figures/dataset_BD_rate_(VMAF)_relative_Energy.jpg)    
     
  


