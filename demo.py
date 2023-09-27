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

