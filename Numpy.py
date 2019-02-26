import numpy as np

#Using Numpy
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2


total_grade= test_1 +test_2 + test_3_fixed 
final_grade = total_grade // 3


#Using List
b=  zip(test_1,test_2 ,test_3)
print(b)

a= []

for i in range(len(b)):
  c=(sum(b[i])) // len(b[i])
  a.append(c)

#Printing Answers
print(final_grade)
print(a)

""" 
Percentiles

As we know, the median is the middle of a dataset: 
it is the number for which 50% of the samples are below, and 50% of the samples are above. 
But what if we wanted to find a point at which 40% of the samples are below, and 60% of the samples are above?

This type of point is called a percentile. 
The Nth percentile is defined as the point N% of samples lie below it. 
So the point where 40% of samples are below is called the 40th percentile.
Percentiles are useful measurements because they can tell us where a particular value is situated within the greater dataset.

In NumPy, we can calculate percentiles using the function np.percentile,
which takes two arguments: the array and the percentile to calculate.

Some percentiles have specific names:

The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile

The difference between the first and third quartile is a value called the interquartile range. 
interquartile range can be calculated as third_quartile - first_quartile

Using the np.sort method to locate outliers.
Calculating central positions of a dataset using np.mean and np.median.
Understanding the spread of our data using percentiles and the interquartile range.
Finding the standard deviation of a dataset using np.std.


"""
