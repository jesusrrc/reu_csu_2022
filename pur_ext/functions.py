"""
Title: PurExt Functions
Author: Vincent Miller
Date: 18 July 2022
Description: Contains the necessary functions to perform the Purpose Extraction implementation
Functions: is_complete(), custom_sentence_end(), rule_extractor(), process_policies(), generate_totals()
"""
import os
import time
import spacy
from spacy import Language
import pandas as pd
import numpy as np


def is_complete(sentence):
    """Checks if sentence is a complete sentence in order to eliminate titles, url button text, garbage strings
       Inputs spaCy sentence span and returns boolean True/False"""
    nouns = 1  # 1 allows simple sentences to pass, 2 excludes simple sentences, gives more complex sentences
    verbs = 1  # a complete sentence must have at least one verb
    n_pos = ["NOUN", "PROPN", "PRON"]  # list for noun pos_
    if sentence[0].is_title and sentence[-1].is_punct:  # if sentence starts with capital and ends with punctuation
        for token in sentence:  # loops through each token to check for noun and verb
            if token.pos_ in n_pos:
                nouns -= 1
            elif token.pos_ == "VERB":
                verbs -= 1
        if nouns < 1 and verbs < 1:  # if sentence contains required noun/verb, sentence is complete
            return True
        else:  # not complete sentence
            return False


@Language.component("component")
def custom_sentence_end(doc):
    """Adding custom pipeline for spacy to include \n as a reference for sentence stops
       Inputs and returns spaCy doc"""
    for token in doc[:-1]:
        if token.text == '\n':
            doc[token.i+1].is_sent_start = True
    return doc


def rule_extractor(doc):
    """Implements PurExt pseudocode to extract the purpose aware rules
       Inputs spaCy doc, Extracts the rules and stores them in a Pandas dataframe, Returns dataframe
       """

    # Word Lists
    # Noun represents purpose (p_nouns) and Contain or Use verb (cou_verbs) from table 1, PurExt paper
    p_nouns = ["purpose", "reason", "intention", "goal", "motivation", "way"]
    cou_verbs = ["access", "check", "collect", "disclose", "gather", "keep", "know", "obtain", "process",
                 "provide", "receive", "request", "retain", "save", "share", "store", "transfer", "update",
                 "use", "utilize"]

    # Linking Verbs
    # Link or Contain verb (LoC_verb), Linking verbs are common, but action verbs can also be linking verbs
    # list from https://assets.ltkcontent.com/files/linkingverbs-yd-pdf.pdf
    # Come in forms of "to be", "to become", and "to seem". Action verbs: smell, taste, touch, see, hear, etc
    # PurExt authors did NOT have a list for linking or containing verbs
    l_verb = ["act", "acted", "am", "appear", "appeared to be", "are", "are being", "be", "became", "become", "can be",
              "come", "could be", "could have come", "did", "do", "does", "fall", "feel", "fell", "felt", "get", "go",
              "got", "grew", "grow", "had", "had become", "had been", "had seemed", "has", "has appeared", "has become",
              "has been", "has seemed", "have", "have appeared", "have become", "have been", "have seemed", "indicate",
              "is", "is being", "is getting", "keep", "look", "looked", "may be", "might be", "might have been", "must",
              "prove", "remain", "remained", "seem", "seemed", "seeming", "seems", "shall be", "shall have been",
              "should be", "should have appeared", "should have been", "smell", "sound", "stay", "stayed", "taste",
              "tasted", "turn", "was", "was being", "went", "were", "will be", "will become", "will have become",
              "will have been", "will seem", "would be"]

    # Containing Verbs
    # PurExt authors did NOT have a list for linking or containing verbs
    c_verb = ["contain", "include"]

    # create initial dataframe
    column_features = ["Type", "Sentence", "Action", "Data Object", "Purpose"]
    df = pd.DataFrame(columns=column_features)

    # beginning of loop for classifier
    for sentence in doc.sents:  # dependency tree is already constructed through nlp()
        if is_complete(sentence):  # check if sentence is complete sentence
            root = sentence.root  # Let p be the root of T
            sent_out = str(sentence)  # store original sentence for rule extraction

            # Checking child of root for lemma_ "be" as that gets classified as "AUX", Changes root if found
            child_list = [child for child in root.children]
            for child in child_list:
                if child.lemma_ == "be":
                    root = child

            # separates noun subject from predicate(purpose) of sentence by root
            full_noun_subject, full_purpose = sentence.text.split(root.text, 1)  # split sentence by root
            nlp = spacy.load("en_core_web_sm")  # loads small english language into nlp
            doc2 = nlp(full_noun_subject)  # tokenize full noun subject, TODO: learn spacy retokenizer
            doc3 = nlp(full_purpose)

            # initialize variables to be checked in classifier
            subject_noun = None
            subject_modifier = None
            subject_data = None
            action = root.lemma_
            data_object = "[]"

            # find first noun subject of sentence, searching inside full noun subject section
            for token in doc2:
                if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                    subject_noun = token
                    break  # only want the first noun, there may be multiple nouns

            # if there is no noun subject, sentence type is Other
            if subject_noun is None:
                sentence_type = "Other"
            else:
                # find the subject modifier and data object from full noun subject
                for token in doc2:
                    if token.dep_ == "pcomp":
                        subject_modifier = token
                        # action = token.text
                    if token.dep_ == "dobj":
                        subject_data = token
                        data_object = token.text

                # if no data object is in noun subject, sentence might be implicit, check for data object in purpose
                if subject_data is None:
                    for token in doc3:
                        if token.dep_ == "dobj":
                            subject_data = token
                            data_object = token.text

                # start PurExt pseudocode for SentenceClassification()
                # lemma_ = base word, "be" is base for (am, is, are, was, were, has been, are being, etc)
                if root.lemma_ in l_verb or root.lemma_ in c_verb:  # if p is a V link or V contain
                    if subject_noun.lemma_ in p_nouns:  # if the subject s of p is a Purpose noun
                        if subject_modifier is not None and subject_modifier.lemma_ in cou_verbs:
                            # if s is modified by complement containing 1+ CoU verb
                            sentence_type = "Explicit"
                        else:
                            sentence_type = "Other"
                    else:
                        sentence_type = "Other"
                elif root.lemma_ in cou_verbs:  # else if p is CoU verb
                    if subject_data is not None and subject_data.dep_ == "dobj":
                        # object of p contains at least one Data Object
                        sentence_type = "Implicit"
                    else:
                        sentence_type = "Other"
                else:
                    sentence_type = "Other"
                # end PurExt pseudocode for SentenceClassification()

            # build entire rule for sentence
            rule_extraction = [sentence_type, sent_out.replace("\n", " "), action, data_object, full_purpose]
            # add rule to dataframe
            df.loc[len(df.index)] = rule_extraction

    # end sentence in doc.sents loop
    return df  # returns dataframe


def process_policies(file_list):
    """Processes all policies, uses performance timers for each process
       Inputs list of files, runs through rule_extractor(), and
       Saves each dataframe to .csv file"""
    nlp = spacy.load("en_core_web_lg")  # loads large english vocabulary
    nlp.add_pipe("component", before='parser')  # add custom spaCy pipe to handle \n
    nlp.max_length = 2000000
    time_list = list()  # create list to store time values for each file

    for file in file_list:
        if file.endswith(".txt"):  # text files only, skips other files
            start_time = time.perf_counter()  # performance timer
            file_name = os.path.splitext(file)[0]  # get file name without file extension
            print("Start Processing File:", file_name, "Process ID:", os.getpid())

            # read file into spaCy's nlp doc
            file_reader = open("Plain Text Policies/" + file, "r", encoding="utf8")
            doc = nlp(file_reader.read())
            file_reader.close()

            # df manipulation
            df = rule_extractor(doc)  # perform classification, rule extraction, and creates df
            df.drop_duplicates(subset="Sentence", keep=False, inplace=True)  # removes duplicate sentences from df
            df.to_csv("Extracted Policies/" + str(file_name) + ".csv")  # export to csv

            end_time = time.perf_counter()  # performance timer end
            total_time = end_time - start_time
            print("End Processing File:", file_name, "Process ID:", os.getpid(), "Time:", f"{total_time:0.2f} seconds")
            time_list.append(total_time)  # save time to list

    print("End Process:", os.getpid(), f"Total Process Time: {sum(time_list):0.2f} seconds")


def generate_totals():
    """
    Generates a totals file from all the policies in "Extracted Policies" folder.
    "Policy", "Total Sentences", "Total Words", "Total Explicit", "Total Implicit", "Total Other",
    "Total Actions", "Total Data Objects", "Total Purposes"
    No Input, Output: Generates "policy_totals.csv" at location of main.py
    """
    files_all = os.listdir("Extracted Policies/")  # puts all files in dir to list

    # create initial dataframe
    column_features = ["Policy", "Total Sentences", "Total Words", "Total Explicit", "Total Implicit", "Total Other",
                       "Total Actions", "Total Data Objects", "Total Purposes"]
    df_final = pd.DataFrame(columns=column_features)

    for file in files_all:
        file_name = os.path.splitext(file)[0]  # get file name without file extension
        df = pd.read_csv("Extracted Policies/" + file, index_col=[0])
        df.replace(to_replace="[]", value=np.nan, inplace=True)  # replace blank with NaN, should have done from start

        # count each type, avoid AttributeError for when [Explicit, Implicit, Other] do not exist
        try:
            explicit_count = df['Type'].value_counts().Explicit
        except AttributeError:
            explicit_count = 0
        try:
            implicit_count = df['Type'].value_counts().Implicit
        except AttributeError:
            implicit_count = 0
        try:
            other_count = df['Type'].value_counts().Other
        except AttributeError:
            other_count = 0

        # save file data to end of df_final
        df_final.loc[len(df_final.index)] = [file_name, len(df.axes[0]), df['Sentence'].str.split().str.len().sum(),
                                             explicit_count, implicit_count, other_count, df['Action'].count(),
                                             df['Data Object'].count(), df['Purpose'].count()]

    df_final.to_csv("policy_totals.csv")  # export to csv
