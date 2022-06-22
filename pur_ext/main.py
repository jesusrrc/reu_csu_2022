"""
Title: PurExt Implementation
Author: Vincent Miller
Date: 13 June 2022
Description: Implement the PurExt algorithm to pull purpose-aware rules from privacy policies
    See notes.txt for more details
"""

import spacy
from spacy import displacy

"""
Candidate sentences filtered by predicate

  Explicit, 1) predicate is Pnoun, 2) Pnoun is modified by a complement that describes the data CoU statement
    This aims to avoid wrong purpose affiliation
  Implicit, contains at least one Data Object
"""
# PurExt examples
s1 = "The purpose of collecting your location data and speed is to analyze your train statistics."
s2 = "The reason of using your name and e-mail address includes website account registration."
# r1({},{“collect”},{“your location data”,”speed”},{“analyze your train statistics”})
# r2({}, {“use”}, {“Your name”, “e-mail address”}, {“website account registration”})

s3 = s1 + " " + s2

nlp = spacy.load("en_core_web_sm")
doc = nlp(s1)

# Noun represents purpose (P_noun) and Contain or Use verb (CoU_verb) from table 1, PurExt paper
P_noun = ["purpose", "reason", "intention", "goal", "motivation", "way"]
CoU_verb = ["access", "check", "collect", "disclose", "gather", "keep", "know", "obtain", "process",
            "provide", "receive", "request", "retain", "save", "share", "store", "transfer", "update",
            "use", "utilize"]

# Link or Contain verb (LoC_verb), Linking verbs are common, but action verbs can also be linking verbs
# list from https://assets.ltkcontent.com/files/linkingverbs-yd-pdf.pdf
# Linking Verbs come in forms of "to be", "to become", and "to seem". Action verbs: smell, taste, touch, see, hear, etc
# TODO: Assumption: Some of these words are redundant because of spaCy's lemmatization. Clean this list up later
L_verb = ["act", "acted", "am", "appear", "appeared to be", "are", "are being", "be", "became", "become", "can be",
          "come", "could be", "could have come", "did", "do", "does", "fall", "feel", "fell", "felt", "get", "go",
          "got", "grew", "grow", "had", "had become", "had been", "had seemed", "has", "has appeared", "has become",
          "has been", "has seemed", "have", "have appeared", "have become", "have been", "have seemed", "indicate",
          "is", "is being", "is getting", "keep", "look", "looked", "may be", "might be", "might have been", "must",
          "prove", "remain", "remained", "seem", "seemed", "seeming", "seems", "shall be", "shall have been",
          "should be", "should have appeared", "should have been", "smell", "sound", "stay", "stayed", "taste",
          "tasted", "turn", "was", "was being", "went", "were", "will be", "will become", "will have become",
          "will have been", "will seem", "would be"]

# Containing verbs
# TODO: Find more words that "represent the meaning of contain", Find synonyms of words, Examine/Correct Other sentences
C_verb = ["contain", "include"]

# explicit = P_noun + (V_link OR V_contain) + Purpose
for sentence in doc.sents:  # Construct a dependency tree structure T of S (nlp() constructed the dep tree)
    print(sentence)
    p = sentence.root  # Let p be the root of T
    noun_subject = None  # initialize in case of no noun subject found
    # noun_subject = [token for token in sentence if token.dep_ == "nsubj"]  # returns as list, I don't like
    for token in sentence:  # find noun subject of sentence
        if token.dep_ == "nsubj":
            noun_subject = token

    # print(p.lemma_)  # lemma_ = base word, "be" is base for (am, is, are, was, were, has been, are being, etc)
    if p.lemma_ in L_verb or p.lemma_ in C_verb:  # if p is a V link or V contain
        print("LoC_verb found:", p.lemma_)
        if noun_subject.text in P_noun:  # if the subject s of p is a P noun
            print("P_noun found:", noun_subject.text)
            # TODO: update below if to check for subject modified by CoU Verb, look for dep_ == "pcomp", "acomp"?
            if noun_subject.text in CoU_verb:
                print("CoU modifying P_noun found:", noun_subject.text)
                print("Sentence is Explicit!")
            else:
                print("Other Sentence (CoU Modifier check)")
        else:
            print("Other Sentence (P_noun check)")
    elif p.lemma_ in CoU_verb:  # else if p is CoU verb
        print("CoU_verb found")
    else:
        print("Other Sentence (LoC_verb check)")

# http://127.0.0.1:5000 to view dependency tree
# displacy.serve(doc, options={"compact": True, "collapse_phrases": True})
