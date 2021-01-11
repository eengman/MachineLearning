# Computes variance and standard deviation of a dataset

import numpy as np
import math


# Function squares all the numbers in the list
# Input: list(float)
# Output: list(float)


def square_list(dataset):
    new_dataset = []
    for x in dataset:
        x *= x
        new_dataset.append(x)
    return new_dataset

# Function computes the variance of a given dataset
# Input: list
# Output: float


def compute_variance(dataset):
    new_dataset = []
    # Find the mean
    mean = np.mean(dataset)
    # Find the differences from the mean and append to a new list
    for x in dataset:
        x = x - mean
        new_dataset.append(x)
    new_dataset = square_list(new_dataset)
    # Find average of the squared differences
    variance = np.mean(new_dataset)
    return variance


def square_root(num):
    return math.sqrt(num)


def compute_std(dataset):
    variance = compute_variance(dataset)
    s_deviation = square_root(variance)
    return s_deviation


# Create an empty list
data = []

# get number of elements as input
n = int(input("Enter the number of elements : "))

# iterate, taking an element and appending to list
for i in range(0, n):
    element = int(input())
    data.append(element)

variance = compute_variance(data)
standard_deviation = compute_std(data)

print("Variance: ", variance)
print("Standard Deviation: ", standard_deviation)
