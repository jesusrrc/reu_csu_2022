"""
Sentence Classifier
Inputs: doc: contain sentences to be classified
        nlp:
"""
import spacy


def sentence_classifier(doc):
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
    # TODO: Assumption: Some of these words are redundant because of spaCy's lemmatization. Clean this list up later
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
    # TODO: Find more that "represent the meaning of contain", Find synonyms of words, Examine/Correct Other sentences
    c_verb = ["contain", "include"]

    # initialize empty lists for each type
    explicit_sentences = []
    implicit_sentences = []
    other_sentences = []

    # beginning of loop for classifier
    for sentence in doc.sents:  # dependency tree is already constructed through nlp()
        # print(sentence)
        root = sentence.root  # Let p be the root of T

        # separate full subject of sentence by root
        full_noun_subject, full_purpose = sentence.text.split(root.text, 1)  # split sentence by root
        nlp = spacy.load("en_core_web_sm")  # loads small english language into nlp
        doc2 = nlp(full_noun_subject)  # tokenize full noun subject, TODO: learn spacy retokenizer

        # initialize variables to be checked in classifier
        subject_noun = None
        subject_modifier = None
        subject_data = None

        # find first noun subject of sentence, searching inside full noun subject section
        for token in doc2:
            if token.pos_ == "NOUN":  # POS returns the part of speech of the given token.
                subject_noun = token
                break  # only want the first noun, there may be multiple

        # if there is no noun subject, sentence is Other AND WE STOP THE OUTERMOST FOR LOOP.
        if subject_noun is None:
            print("Found None", sentence)
            other_sentences.append(sentence)
            break

        # find the subject modifier and data object from full noun subject
        for token in doc2:
            if token.dep_ == "pcomp":
                subject_modifier = token
            if token.dep_ == "dobj":
                subject_data = token

        # if no data object is in full noun subject, sentence might be implicit, check for data object in purpose
        if subject_data is None:
            for token in doc:
                if token.dep_ == "dobj":
                    subject_data = token

        # commented print statements are my visual debugger
        # print("Noun:", subject_noun, "Modifier:", subject_modifier, "Data:", subject_data.dep_)

        # lemma_ = base word, "be" is base for (am, is, are, was, were, has been, are being, etc)
        if root.lemma_ in l_verb or root.lemma_ in c_verb:  # if p is a V link or V contain
            # print("LoC_verb found:", root.lemma_)
            if subject_noun.text in p_nouns:  # if the subject s of p is a P noun
                # print("p_noun found:", subject_noun.text)
                if subject_modifier.lemma_ in cou_verbs:  # if s is modified by complement containing 1+ CoU verb
                    # print("CoU modifying p_noun found:", subject_modifier.lemma_)
                    explicit_sentences.append(sentence)
                else:
                    # print("Other Sentence (CoU Modifier check)", subject_modifier.lemma_)
                    other_sentences.append(sentence)
            else:
                # print("Other Sentence (p_noun check)")
                other_sentences.append(sentence)
        elif root.lemma_ in cou_verbs:  # else if p is CoU verb
            # print("cou_verbs found", root.lemma_)
            if subject_data.dep_ == "dobj":  # object of p contains at least one Data Object
                # print("Sentence is Implicit!")
                implicit_sentences.append(sentence)
            else:
                # print("Other Sentence (CoU check)")
                other_sentences.append(sentence)
        else:
            # print("Other Sentence (LoC_verb check)")
            other_sentences.append(sentence)

    print("Explicit Sentences:", explicit_sentences)
    print("Implicit Sentences:", implicit_sentences)
    print("Other Sentences:", other_sentences)

    print("Explicit Length:", len(explicit_sentences), "Implicit Length:", len(implicit_sentences),
          "Other Length:", len(other_sentences))"""
PurExt Sentence Classifier
Inputs: doc: contain sentences to be classified
        nlp:
"""
import spacy


def sentence_classifier(doc):
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
    # TODO: Assumption: Some of these words are redundant because of spaCy's lemmatization. Clean this list up later
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
    # TODO: Find more that "represent the meaning of contain", Find synonyms of words, Examine/Correct Other sentences
    c_verb = ["contain", "include"]

    # initialize empty lists for each type
    explicit_sentences = []
    implicit_sentences = []
    other_sentences = []

    # beginning of loop for classifier
    for sentence in doc.sents:  # dependency tree is already constructed through nlp()
        # print(sentence)
        root = sentence.root  # Let p be the root of T

        # separate full subject of sentence by root
        full_noun_subject, full_purpose = sentence.text.split(root.text, 1)  # split sentence by root
        nlp = spacy.load("en_core_web_sm")  # loads small english language into nlp
        doc2 = nlp(full_noun_subject)  # tokenize full noun subject, TODO: learn spacy retokenizer

        # initialize variables to be checked in classifier
        subject_noun = None
        subject_modifier = None
        subject_data = None

        # find first noun subject of sentence, searching inside full noun subject section
        for token in doc2:
            if token.pos_ == "NOUN":
                subject_noun = token
                break  # only want the first noun, there may be multiple

        # if there is no noun subject, sentence is Other
        if subject_noun is None:
            print("Found None", sentence)
            other_sentences.append(sentence)
            break

        # find the subject modifier and data object from full noun subject
        for token in doc2:
            if token.dep_ == "pcomp":
                subject_modifier = token
            if token.dep_ == "dobj":
                subject_data = token

        # if no data object is in full noun subject, sentence might be implicit, check for data object in purpose
        if subject_data is None:
            for token in doc:
                if token.dep_ == "dobj":
                    subject_data = token

        # commented print statements are my visual debugger
        # print("Noun:", subject_noun, "Modifier:", subject_modifier, "Data:", subject_data.dep_)

        # lemma_ = base word, "be" is base for (am, is, are, was, were, has been, are being, etc)
        if root.lemma_ in l_verb or root.lemma_ in c_verb:  # if p is a V link or V contain
            # print("LoC_verb found:", root.lemma_)
            if subject_noun.text in p_nouns:  # if the subject s of p is a P noun
                # print("p_noun found:", subject_noun.text)
                if subject_modifier.lemma_ in cou_verbs:  # if s is modified by complement containing 1+ CoU verb
                    # print("CoU modifying p_noun found:", subject_modifier.lemma_)
                    explicit_sentences.append(sentence)
                else:
                    # print("Other Sentence (CoU Modifier check)", subject_modifier.lemma_)
                    other_sentences.append(sentence)
            else:
                # print("Other Sentence (p_noun check)")
                other_sentences.append(sentence)
        elif root.lemma_ in cou_verbs:  # else if p is CoU verb
            # print("cou_verbs found", root.lemma_)
            if subject_data.dep_ == "dobj":  # object of p contains at least one Data Object
                # print("Sentence is Implicit!")
                implicit_sentences.append(sentence)
            else:
                # print("Other Sentence (CoU check)")
                other_sentences.append(sentence)
        else:
            # print("Other Sentence (LoC_verb check)")
            other_sentences.append(sentence)

    print("Explicit Sentences:", explicit_sentences)
    print("Implicit Sentences:", implicit_sentences)
    print("Other Sentences:", other_sentences)

    print("Explicit Length:", len(explicit_sentences), "Implicit Length:", len(implicit_sentences),
          "Other Length:", len(other_sentences))
