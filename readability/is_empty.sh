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
myarray=`ls results_final`

# Getting readability results.
for x in $myarray 
  do

  # Checking for empty files.
  if [ ! -s "results_final/${x}" ]; then
    mv "results_final/${x}" ./../empty_profiles
  fi

  done
