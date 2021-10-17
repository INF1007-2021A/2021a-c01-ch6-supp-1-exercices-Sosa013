#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools

# Question 1
def get_maximums(numbers):
	list_initial = [numbers]
	new_list = []
	for numbers in list_initial:
		for elem in numbers:
			list_initial = new_list.append(max(elem))

	return new_list

# [max(elem) for elem in numbers] sa marche aussi bien

# Question 2
def join_integers(numbers):

	return int("".join(([str(elem) for elem in numbers])))

# Question 3
def generate_prime_numbers(limit):
	return [0]

# Question 4
def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [""]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
