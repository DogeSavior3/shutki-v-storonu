#!/bin/bash
#SBATCH --job-name="clean_texts"
#SBATCH -c 4
#SBATCH --nodes=1
#SBATCH --time=0-1:0
#SBATCH --mail-user=mvkorol@edu.hse.ru
#SBATCH --mail-type=ALL

module purge
module load Python
conda deactivate
conda activate hebrew
python cleaner.py
