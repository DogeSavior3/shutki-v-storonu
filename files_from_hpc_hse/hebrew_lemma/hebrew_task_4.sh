#!/bin/bash
#SBATCH --job-name="hebrew_lemmatization"
#SBATCH -c 16
#SBATCH --gpus=2
#SBATCH --constraint="type_e"
#SBATCH --time=0-5:0

module purge
module load Python
conda deactivate
conda activate hebrew

CUDA_VISIBLE_DEVICES=0 python stanza_gpu_97.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_98.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_99.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_100.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_101.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_102.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_103.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_104.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_105.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_106.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_107.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_108.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_109.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_110.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_111.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_112.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_113.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_114.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_115.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_116.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_117.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_118.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_119.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_120.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_121.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_122.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_123.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_124.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_125.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_126.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_127.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_128.py &

wait
