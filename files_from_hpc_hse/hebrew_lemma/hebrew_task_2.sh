#!/bin/bash
#SBATCH --job-name="hebrew_lemmatization"
#SBATCH -c 32
#SBATCH --gpus=8
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
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_8.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_9.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_10.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_11.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_12.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_13.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_14.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_15.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_16.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_17.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_18.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_19.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_20.py &
CUDA_VISIBLE_DEVICES=2 python stanza_gpu_21.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_22.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_23.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_24.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_25.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_26.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_27.py &
CUDA_VISIBLE_DEVICES=3 python stanza_gpu_28.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_29.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_30.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_31.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_32.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_33.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_34.py &
CUDA_VISIBLE_DEVICES=4 python stanza_gpu_35.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_36.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_37.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_38.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_39.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_40.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_41.py &
CUDA_VISIBLE_DEVICES=5 python stanza_gpu_42.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_43.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_44.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_45.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_46.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_47.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_48.py &
CUDA_VISIBLE_DEVICES=6 python stanza_gpu_49.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_50.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_51.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_52.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_53.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_54.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_55.py &
CUDA_VISIBLE_DEVICES=7 python stanza_gpu_56.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_57.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_58.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_59.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_60.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_61.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_62.py &
CUDA_VISIBLE_DEVICES=8 python stanza_gpu_63.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_64.py &

wait

