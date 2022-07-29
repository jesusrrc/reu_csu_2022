"""
Title: PurExt Implementation Readme
Author: Vincent Miller
Date: 18 July 2022
Files: main.py, functions.py, policy_totals.csv, README.txt
Folders: Extracted Policies, Plain Text Policies
"""

main.py
  In order to run main.py, plain text policies must be in the Plain Text Policies
  folder and saved as .txt file type. This code allows for multiprocessing which
  is controlled by a boolean variable that is defaulted to True. This code defaults
  to 8 processes which can be controlled by the user. The files_all will be split
  according to how many processes there are, so each process gets an equal amount
  of files to policies. There are performance timers so the user may track how long
  each policy takes and how long the overall process takes.

functions.py
  This file contains necessary functions to complete the Purpose Extraction
  implementation. 
  is_complete() checks for complete sentences. 
  custom_sentence_end() adds to the spacy pipeline for the inclusion of \n at 
    the end of sentences.
  rule_extractor() does the bulk of the heavy lifting. It applies the pseduocode
    provided by the PurExt authors and returns a pandas dataframe.
  process_policies() calls the rule_extractor() while using performance timers
    to keep track of how long each policy takes. This also exports each dataframe
    to a csv file saved in the folder "Extracted Policies."
  generate_totals() creates policy_totals.csv which contains the totals for 
    "Policy", "Total Sentences", "Total Words", "Total Explicit", "Total Implicit", "Total Other",
    "Total Actions", "Total Data Objects", "Total Purposes"

PurExt Reference:
Lu Yang, Xingshu Chen, Yonggang Luo, Xiao Lan, Li Chen, 
"PurExt: Automated Extraction of the Purpose-Aware Rule from the Natural 
Language Privacy Policy in IoT", Security and Communication Networks, 
vol. 2021, Article ID 5552501, 11 pages, 2021. 
https://doi.org/10.1155/2021/5552501

PurExt Algorithm, SentenceClassification() Pseudocode
    Input: a sentence S to be classified
    Output: a sentence category label in (E, I, O)
        where E for explicit sentence
        where I for implicit sentence
        where O for other sentences
     1, Construct dependecy tree structure T of S
     2, Let p be the root of T
     3, if p is Verb_link OR Verb_contain
     4,     if subject s of p is P_noun
     5,         if s is modified by a complement containing at least one Verb_CoU
     6,             return E
     7,         else
     8,             return O
     9,         end if
    10,     else
    11,         return O
    12,     end if 
    13, else if p is Verb_CoU
    14,     if object of p contains at least one Data Object
    15,         return I
    16,     else
    17,         return O
    18,     end if
    19, else
    20,     return O
    21, end if

Word Lists
    Verb_CoU = Access, check, collect, disclose, gather, keep, know, obtain, process, provide, receive, request, retain, save, share, store, transfer, update, use, utilize
    Pnoun = Purpose, reason, intention, goal, motivation, way
