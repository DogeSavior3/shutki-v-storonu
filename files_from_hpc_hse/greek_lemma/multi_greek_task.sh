#!/bin/bash
#SBATCH --job-name="greek_lemma_threads_gpu"
#SBATCH -c 32
#SBATCH --gpus=2
#SBATCH --nodes=1
#SBATCH --time=3-0:0
#SBATCH --mail-user=mvkorol@edu.hse.ru
#SBATCH --mail-type=ALL

module purge
module load Python
conda deactivate
conda activate hebrew
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_1.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_2.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_3.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_4.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_5.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_6.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_7.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_8.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_9.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_10.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_11.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_12.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_13.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_14.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_15.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_greek_16.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_17.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_18.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_19.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_20.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_21.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_22.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_23.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_24.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_25.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_26.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_27.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_28.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_29.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_30.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_31.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_greek_32.py &

wait