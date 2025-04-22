#!/bin/bash
#SBATCH --job-name="greek_lemmatization"
#SBATCH -c 1
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --time=2-0:0
#SBATCH --mail-user=mvkorol@edu.hse.ru
#SBATCH --mail-type=ALL

module purge
module load Python
conda deactivate
conda activate hebrew
python stanza_gpu_greek.py
