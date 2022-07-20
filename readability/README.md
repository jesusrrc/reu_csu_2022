# readability: Readability Assessment of Our Dataset of Privacy Policies.

## Description

This folder contains the files/scripts used perform readability assessments and visualize these metrics with scatterplots.
We used an external Python package to obtain these metrics [1].

We retrieved and recorded the following metrics:
* Kincaid Grade Level.
* Automated Readability Index (ARI).
* Coleman-Liau Index.
* Flesch Reading Ease Test.
* Gunning Fog Index.
* Lix Readability Formula.
* SMOG Readability Formula.
* Rix Readability Test.
* Dale-Chall Index.
* Characters per Word.
* Syllables per Word.
* Words per Sentence.
* Number of Characters.
* Number of Syllables.
* Number of Words.
* Number of Sentences.
* Number of Be Verbs.
* Number of Auxilliary Verbs.
* Number of Conjunctions.
* Number of Pronouns.
* Number of Prepositions.

<p align="center">
  <figure>
  <img width="700" src="https://github.com/jesusrrc/reu_csu_2022/blob/main/readability/plots/example.png">
  <figcaption>Figure: Sample Scatterplot for a Readability Metric.</figcaption>
  </figure>
</p>

## Files/Scripts

* `assessmentIOT.py`: Python script to build readability profile for a privacy policy specified by a command-line
argument specifying the path to the text file.
* `get_assessments_IOT.sh`: Bash script that calls `assessmentIOT.py` to build the readability profile for each
privacy policy.
* `extract_valid.py`: Python script to find valid privacy policies (policies with 100 or more words).
* `report.py`: Python script to produce metrics report and the scatterplots for each metric.
* `results_final`: A folder with the readability reports for each privacy policy.
* `plot`: A folder with the 20+ scatterplots for each readability metric.

## Compilation

To obtain the resulting files, please run this Bash script, which assumes the folder `results_final` has been created:

    ./get_assessments_IOT.sh

Then, we can extract the valid privacy policies based on the readability assessments:

    python3 extract_valid.py

Afterwards, we can build a general readability report and the scatterplots for each metric:

    python3 report.py

## References

[1] https://pypi.org/project/readability/
