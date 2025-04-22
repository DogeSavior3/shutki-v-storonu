#!/bin/bash
#SBATCH --job-name="greek_lemma_threads_cpu"
#SBATCH -c 8
#SBATCH --time=2-0:0
#SBATCH --mail-user=mvkorol@edu.hse.ru
#SBATCH --mail-type=ALL

module purge
module load Python
conda deactivate
conda activate hebrew
python stanza_cpu_base_1.py &
python stanza_cpu_base_2.py &
python stanza_cpu_base_3.py &
python stanza_cpu_base_4.py &
python stanza_cpu_base_5.py &
python stanza_cpu_base_6.py &
python stanza_cpu_base_7.py &
python stanza_cpu_base_8.py &

wait