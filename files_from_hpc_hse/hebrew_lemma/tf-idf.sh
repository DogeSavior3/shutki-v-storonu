#!/bin/bash
#SBATCH --job-name="hebrew_lemmatization"
#SBATCH -c 16
#SBATCH --time=0-12:0

module purge
module load Python
conda deactivate
conda activate hebrew

python tf-idf.py
