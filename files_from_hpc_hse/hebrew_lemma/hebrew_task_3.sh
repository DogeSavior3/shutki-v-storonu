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

CUDA_VISIBLE_DEVICES=0 python stanza_gpu_33.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_34.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_35.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_36.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_37.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_38.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_39.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_40.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_41.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_42.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_43.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_44.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_45.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_46.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_47.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_48.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_49.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_50.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_51.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_52.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_53.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_54.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_55.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_56.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_57.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_58.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_59.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_60.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_61.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_62.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_63.py &
CUDA_VISIBLE_DEVICES=0 python stanza_gpu_64.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_65.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_66.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_67.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_68.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_69.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_70.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_71.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_72.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_73.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_74.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_75.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_76.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_77.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_78.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_79.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_80.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_81.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_82.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_83.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_84.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_85.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_86.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_87.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_88.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_89.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_90.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_91.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_92.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_93.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_94.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_95.py &
CUDA_VISIBLE_DEVICES=1 python stanza_gpu_96.py &

wait
