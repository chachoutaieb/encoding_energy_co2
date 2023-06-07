# @Developed by Chachou Taieb (°_^)
#!/usr/bin/env python3
import os


python3 '/path to the project folder/encoding_energy_co2.py' \
      -d '/path to the project folder/original_dataset' \
      -r '/path to the project folder/encoding_resultsCPU.xlsx' \
      -p CPU \
      -sp faster \
      -it  0.04  0.1 0.2 1 0.2 \
      -m psnr ssim vmaf 


python3 '/path to the project folder/encoding_energy_co2.py'  \
      -i '/path to the project folder/original_dataset/BasketballPass_416x240_50.yuv' \
      -o '/path to the project folder/original_dataset/outputVideo.mp4' \
      -r '/path to the project folder/encoding_resultsCPU.xlsx' \
      -s 416x240 \
      -f 50 \
      -x 8 \
      -b 500 \
      -c x264 \
      -p CPU \
      -sp slower \
      -it 0.3 \
      -m psnr ssim vmaf


