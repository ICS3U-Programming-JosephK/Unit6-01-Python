#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: December 13
# This program generates numbers from 0-100 ten times
# and outputs the average

import random


def main():
    # Creating empty list and "total_sum" variable
    nums = []
    total_sum = 0

    # Generating the 10 random numbers
    for counter in range(10):
        random_num = random.randint(0, 100)
        nums.append(random_num)
        print("{} added to list at index {}".format(random_num, counter))

    # Calculating the sum of the list
    for counter in range(10):
        total_sum += nums[counter]

    average = total_sum / 10

    # Displaying the average
    print()
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
