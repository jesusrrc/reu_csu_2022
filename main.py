"""
Title: PurExt Implementation
Author: Vincent Miller
Date: 18 July 2022
Description: Implement the Purpose Extraction (PurExt) algorithm to extract purpose-aware rules from privacy policies.
Files: main.py - controls how many processes to split the workload, and calls the process_policies() function.
       functions.py - required file, contains necessary functions that perform the bulk of the work.
Input: Plain text (.txt) files stored in folder "Plain Text Policies/".
Output: Comma Separated Values (.csv) files stored in folder "Extracted Policies/".
"""
import os
import time
import multiprocessing
import functions

multiprocess = True  # turn on/off multiprocess
process = 8  # how many processes to use, and how many splits to perform on dir list
files_all = os.listdir("Plain Text Policies/")  # puts all files in dir to list

if multiprocess:
    # split files into even lists for each process
    files_split = [files_all[i:i + process] for i in range(0, len(files_all), process)]
    if __name__ == "__main__":  # main check gate
        start_time = time.perf_counter()  # start performance timer
        pool = multiprocessing.Pool(processes=process)  # initialize multiple processes
        pool.map(functions.process_policies, files_split)  # start processes for function and input
        end_time = time.perf_counter()  # end performance timer
        print(f"Total Time: {end_time - start_time:0.2f} seconds")
else:
    functions.process_policies(files_all)

# functions.generate_totals()

# display dependency tree for sentence at http://127.0.0.1:5000
# displacy.serve(doc)  # options={"compact": True, "collapse_phrases": True}
