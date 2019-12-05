#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def sum_of_numbers(list_of_numbers):
    # this functions find the largest value

    largest = list_of_numbers[0]

    for counter in range(1, len(list_of_numbers)):
        if largest < list_of_numbers[counter]:
            largest = list_of_numbers[counter]

    return largest


def main():
    # this function uses a list

    random_numbers = []

    # input
    print("The numbers are ")
    for loop_counter in range(0, 4):
        a_single_number = random.randint(0, 5)
        random_numbers.append(a_single_number)
        print("The random numbers are: {}".format(a_single_number))
    largest = sum_of_numbers(random_numbers)
    print("The largest number is: {0}".format(largest))


if __name__ == "__main__":
    main()
