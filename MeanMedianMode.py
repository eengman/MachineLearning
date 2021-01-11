import numpy as np
import matplotlib.pyplot as plt

# Mean Vs Median
# Lets create some fake income data, centered around 27,000 with a normal distribution and standard deviation of 15,000,
# with 10,000 data points. (We"ll discuss those terms more later, if you're not familiar with them.)

# Then, compute the mean (average) - it should be close to 27,000:
incomes = np.random.normal(27000, 15000, 10000)
mean_of_incomes = np.mean(incomes)
print("Incomes: ", incomes)
print("Mean of Incomes: ", mean_of_incomes)

# We can segment the income data into 50 buckets, and plot it on a histogram
plt.hist(incomes, 50)
# plt.show()

# Now compute the median
print("Median: ", np.median(incomes))

# Now we add Jeff Bezos, observe how it will mess up the mean
incomes = np.append(incomes, [1000000000])
print("Mean with Jeff Bezos: ", np.mean(incomes))

# Mode
# Generate some fake age data for 500 ppl
# ages = np.random.randint(18, high=90, size=500)
# ages
# stats.mode(ages)
