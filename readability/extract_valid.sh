#########################################################################################
#
# REU@CSU 2022
#
# Author:      Jesus Rafael Rijo Candelario (Mercer University)
# Date:        07/05/2022
# Advisor:     Dr. Lydia Ray
# Description: Bash script to call readability assessment script for several datasets in
#              get_policies/clean_policies.
#
#########################################################################################

# Getting the names of all the IoT privacy policies.
myarray=`ls results`

# Getting readability results.
for x in $myarray 
  do
  x="results/${x}"
  python3 extract_valid.py $x 
  done
