# Energy and Carbon Emissions of Modern Video Encoders
In this project,  we provide a comparative study between different video encoder standard namely H.264/AVC, H.265/HEVC, VVC, VP9, and AV1,  in terms of quality, energy consumption and carbon emissions. This study allows  to better understand the trade-off between quality and encoding carbon emissions of different encoder and determine which one is the most appropriate for climate change.

## Install 


```bash
git clone https://github.com/chachoutaieb/encoding_energy_co2.git
pip3 install -r requirements.txt

```

## Download Dataset

- [x] [Original dataset](https://jvet.hhi.fraunhofer.de/)
- [x] [Encoded dataset](https://drive.google.com/uc?export=download&id=1ahQP7uaV7-ENN5bSBzgW3GAN72bnya6s)

## Usage

```bash

python3 /your-path-to-the-project/encoding_video.py
-s /your-path-to-the-project/original_dataset \
-t '/your-path-to-the-project/encoding_results.xlsx' \
-v 'CPU' -m psnr ssim vmaf


```
energy and CO2 emissions   |  Encoding time               |  CPU and memory usage        | 
:-----------------------------:|:----------------------------:|:-----------------------------:
![](figures/Bar_dataset.jpg)   |  ![](figures/Bar_dataset.jpg)      ![](figures/Bar_dataset.jpg)



