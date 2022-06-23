#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        06/23/2022
# Advisor:     Dr. Lydia Ray
# Description: Bash script to call readability assessment script for several datasets in
#              old_datasets.
#
#########################################################################################

# Piping outputs to text files.
#python3 assessment.py ./../old_datasets/carnegie_corpus.csv 0 > assessment_1
#python3 assessment.py ./../old_datasets/opp-155_corpus.csv 0  > assessment_2
python3 assessment.py ./../old_datasets/final_fixed_purext-600_corpus.csv 1 > assessment_3
