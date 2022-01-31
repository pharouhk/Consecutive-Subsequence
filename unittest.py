import pandas as pd
import numpy as np
import find_subsequence as f


def _print_success_message():
    
    print('Tests Passed!')

def test_subsequence():
	assert f.highest_consecutive_sum([1,2,3,4]) == 10, 'The maximum consecutive sequence sum is incorrect'
	assert f.highest_consecutive_sum([2,4,6,8]) == 20, 'The maximum consecutive sequence sum is incorrect'
	assert f.highest_consecutive_sum([-2,4,-3,3,1,0,2,-1]) == 4, 'The maximum consecutive sequence sum is incorrect'

	_print_success_message()