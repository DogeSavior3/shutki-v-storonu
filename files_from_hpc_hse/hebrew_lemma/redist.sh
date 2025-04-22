#!/bin/bash
#SBATCH --job-name="clean_texts"
#SBATCH -c 1
#SBATCH --nodes=1
#SBATCH --time=0-0:30
#SBATCH --mail-user=mvkorol@edu.hse.ru
#SBATCH --mail-type=ALL

module purge
module load Python
conda deactivate
conda activate hebrew
python redist.py
