# readability: Automated Extraction and Preprocessing of IoT Privacy Policies.

## Description

This folder contains the files/scripts used to gather IoT privacy policies as HTML files from the web and preprocess these files
into plaintext files.

## Files/Scripts

* `links_7`: Text file with links to the HTML files.
* `get_policies.py`: Python script to retrieve HTML IoT privacy policies.
* `clean_policies.py`: Python script to clean HTML IoT privacy policies in `raw_policies`.
* `raw_policies`: Folder with HTML IoT privacy policies.
* `clean_policies`: Folder with cleaned plaintext IoT privacy policies.

## Compilation

To obtain the raw HTML files, run this Python scripts, procuring `raw_policies` and `links_7` are in the same directory:

    python3 get_policies.

Then, we can convert the HTML files into plaintext files, procuring `cleaned_policies` exists in the current directory:

    python3 extract_valid.py

## References

[1] https://www.crummy.com/software/BeautifulSoup/bs4/doc/
