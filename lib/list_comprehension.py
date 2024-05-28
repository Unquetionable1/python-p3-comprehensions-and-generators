#!/usr/bin/env python3
num_list=[1,2]
def return_evens(num_list):
    # Correct list comprehension to filter out even numbers
    evens = [num for num in num_list if num % 2 == 0]
    return evens


print(return_evens(num_list))


def make_exclamation(sentence_list):
    
    return [sent +'!' for sent in sentence_list  if len(sentence_list) > 0 ]
print(make_exclamation(sentence_list=['s','m','n']))
