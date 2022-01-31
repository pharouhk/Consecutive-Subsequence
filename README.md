# Simple software to calculate susequence with highest sum

This repository contains code and associated files for calculating the consecutive subsequence with the highest sum.This solution runs in the O(nLogn) which is mostly the time complexity of the sorting operation. Other operations are neglible as n approaches infinity.
References: [geeksforgeeks](https://www.geeksforgeeks.org/longest-consecutive-subsequence/)

## Background/Introduction
Nowadays, IOT systems  collect an enormous amount of  sensory data every second. To make use of this large pool of sensory data in a  pipeline, you might need to identify interesting subsequences. The project is an abstraction of this, with the list of integers representing the sensor data and the sum is the metric to evaluate if a subsequence is interesting. The goal of this project is to enable users to quickly obtain the highest sum from a list of integers.

## High Level Flow
* User Input: *python find_subsequence.py source_data max_subsequence_length*
    - source_data (mandatory): Specifies the file path where the data is stored. A text file containing integers is the expected format.
    - max_subsequence_length (optional): Specifies the maximum possible subsequence length that can be considered.

* Output: Highest sum as an integer



### Steps to run the code

* git clone this repository at https://github.com/pharouhk/Consecutive-Subsequence.git to quickly get the source code and all other dependencies.
* You will see the following file structure below:
    - _pycahce_
    - sensordata
        - input_1.txt
        - input_2.txt
        - input_3.txt
    - READme.md
    - find_subsequence.py
    - requirements.txt
    - unittest.py
* Open the command line and run the following command. The run command requires a file path to be passed as an argument and an optional numeric argument.
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
