# Simple software to calculate susequence with highest sum

This repository contains code and associated files for calculating the consecutive subsequence with the highest sum.This solution runs in the O(nLogn) which is mostly the time complexity of the sorting operation. Other operations are neglible as n approaches infinity.
References: [geeksforgeeks](https://www.geeksforgeeks.org/longest-consecutive-subsequence/)

### Steps to run the code

* Extract the compressed ('tar.gz') file to receive the necessary files.
* You will see the following file structure below:
    - _pycahce_
    - new_env
    - sensordata
        - input_1.txt
        - input_2.txt
        - input_3.txt
    - find_subsequence.py
    - requirements.txt
    - unittest.py
* Open the command line and run the following command
    ```
    cd folder_name/Consecutive Subsequence
    pip install -r requirements.txt
    python find_subsequence.py sensordata/input_1.txt 2
    ```
 * Your result would be displayed in the stdout in the command line
 * The unit tests can be run using the following command
    ```
    python
    import unittest as u
    u.test_subsequence()
    ```
 * You should get "Tests Passed!" output
