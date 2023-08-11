import numpy as np

def greet_module_b():
    return "Greeting from Module B!"

def perform_calculations():
    numbers = np.array([1,2,3,4,5])
    sum_numbers = np.sum(numbers)
    average = np.mean(numbers) # NumPy method for average
    return sum_numbers, average