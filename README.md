# Energy and Carbon Emissions of Modern Video Encoders
In this project,  we provide a comparative study between different video encoder standard namely H.264/AVC, H.265/HEVC, VVC, VP9, and AV1,  in terms of quality, energy consumption and carbon emissions. This study allows  to better understand the trade-off between quality and encoding carbon emissions of different encoder and determine which one is the most appropriate for climate change.

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


  energy and CO2 emissions     |  CPU and memory usage         |  Encoding time                | 
:-----------------------------:|:-----------------------------:|:-----------------------------:
 ![](figures/Bar_dataset.jpg)  | ![](figures/bar_cpu_memory_time.jpg)  |  ![](figures/line_dataset_time.jpg)   
 
 ### Quality
 ```
           PSNR                |             SSIM              |              VMAF             | 
:-----------------------------:|:-----------------------------:|:------------------------------:
 ![](figures/Bar_daet.jpg)  | ![](figures/bar_cpu_memory_ti.jpg)  |  ![](figures/ time.jpg)    |



