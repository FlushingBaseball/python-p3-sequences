#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
         sequence =[0,1]
         while len(sequence) < length:
             next_value = sequence[len(sequence) -1] + sequence[len(sequence) -2]
             sequence.append(next_value)
         print(sequence)

   