# get_policies_links: Extraction of Links to Privacy Policies.

## Description

This folder contains the files/scripts used to retrieve links to privacy policies from the web [1]. After finishing this portion of
the project, we obtained about 3000 links to privacy policies from Google.

## Files/Scripts

* `get_policies_links.py`: Python script to extract links to IoT privacy policies from the web.
* `iot_names_3`: Text file with names of IoT companies. 

## Compilation

To obtain the files, please run this Python script and pipe its output into a text file:

    python3 get_policies_links.py | iot_links_7

## References

[1] https://pypi.org/project/googlesearch-python/
