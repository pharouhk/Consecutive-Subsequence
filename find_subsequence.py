#!/usr/bin/env python 3.7

import pandas as pd
import numpy as np
import argparse




def read_file(file_path):
	with open(file_path) as f:
		lines = f.readlines()
	return lines



def highest_consecutive_sum(num_list, limit=None):
	'''
	function that returns the consecutive subsequence with the highest sum.
	:param num_list: this is a list of integers gotten from a text file
	:param limit: this is an optional parameter that limits the size of the subsequence. The default is None.
	return: A single value representing the highest sum
	'''
	
	#if num_list is empty return 0
	if not num_list:
		return 0

	streak_sum = {} #dictionary to store the subsequences and their sums
	num_list.sort() #sorting o an ordered list
    
	current_streak = [num_list[0]] #this would be where we would store the subsequences in the list
	v = [num_list[0]] #the logic below helps to de-duplicate the list
	
	for i in range(1, len(num_list)):
		if (num_list[i] != num_list[i - 1]):
			v.append(num_list[i])

	#the logic below retrieves the maximum consecutive difference
	consecutive_diff = [b - a for a, b in zip(v, v[1:])]
	max_diff = max(consecutive_diff)

	for n in range(1, max_diff+1): #iterating from 1 to the maximum consecutive difference (1,2,...,max_diff)
		streak_sum[str(current_streak)] = sum(current_streak[:limit])#first, save the sum of the current subsequence
		current_streak = [num_list[0]] # reset the current subsequence to the start of the list
		for i in range(1, len(v)): #iterating through the sorted de-duplicated list v
			if (i > 0 and v[i] == v[i - 1] + n): #conditions to check if the next value is the previous value + n 
				current_streak.append(v[i]) #add this value to the ongoing streak 
			else:
				streak_sum[str(current_streak)] = sum(current_streak[:limit]) #first, save the sum of the current subsequence
				current_streak = [] # reset the current subsequence
				current_streak.append(v[i]) #keep the latest value to track the next subsequence
	
	longest_streak_sum = max(list(streak_sum.values())) #saves the highest sum
	#the logic below returns the maximum sum between the last subsequence and highest saved subsequence.
	if len(current_streak)>1: #checks if the current subsequence is a streak
		highest_sum = max(longest_streak_sum, sum(current_streak[:limit])) #chooses the maximum between the last subsequence and the highest sum
	else:
		highest_sum = longest_streak_sum #if the condition above is not met, the highest sum is the desired result
	return highest_sum

def main(cl_params):
	'''
	function that glues everything. It receives the command line arguments, preprcess it before sending to the highest_consecutive_sum function
	:param cl_paramas: these parameter holds command line arguments - file path and limit n
	return: A single value representing the highest sum
	'''

	input_data = read_file(cl_params.filename)
	input_data = input_data[0].split('\n')[0].split(' ')
	input_data = [int(val) for val in input_data]

	highest_cs = highest_consecutive_sum(input_data, cl_params.restrict)
	return highest_cs


if __name__ == "__main__":
	# Initialize command line parser
	parser = argparse.ArgumentParser()

	#Read arguments from command line
	parser.add_argument('filename', type=str) #this argument is required
	parser.add_argument('restrict', nargs = '?',type=int, default = None) #second argument but optional
	args = parser.parse_args()
	result = main(args)
	print(result)