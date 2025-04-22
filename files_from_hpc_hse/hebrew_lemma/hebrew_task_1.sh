#!/bin/bash
#SBATCH --job-name="hebrew_lemmatization"
#SBATCH -c 32
#SBATCH --gpus=2
#SBATCH --constraint="type_e"
#SBATCH --time=0-12:0

module purge
module load Python
conda deactivate
conda activate hebrew

CUDA_VISIBLE_DEVICES=0 python stanza_gpu_1.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_2.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_3.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_4.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_5.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_6.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_7.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_8.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_9.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_10.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_11.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_12.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_13.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_14.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_15.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_16.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_17.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_18.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_19.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_20.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_21.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_22.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_23.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_24.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_25.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_26.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_27.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_28.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_29.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_30.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_31.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_32.py &

wait
