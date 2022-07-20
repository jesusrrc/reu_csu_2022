# get_names: Name Extraction of IoT Companies

## Description

This folder contains the files/scripts used to extract names of IoT companies from iotone.com. IoT ONE is an American development firm that
specializes on devising IoT solutions for companies throughout Asia [1].

## Files/Scripts

* `get_policy_names_iotone.py`: Python script used to extract names from iotone.com. The output of this
script should be piped to a file named iot_names.
* `output.html`: An HTML file with the raw IoT company names [2].
* `iot_names_3`: A text file with the actual names of IoT companies. Note that this file may contain repeated
tokens. Additionally, any other text files named similarly to `iot_names` are obsolete.

## Compilation

To extract the names, please run the script in this fashion on a Linux terminal, like Ubuntu:

    python3 get_policy_names_iotone.py | iot_names.txt

## References

[1] https://www.iotone.com/about </br> 
[2] https://www.iotone.com/suppliers
