#
#
# import matplotlib.pyplot as plt
#
# labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
# sizes = [38.4, 40.6, 20.7, 10.3]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# patches, texts = plt.pie(sizes, colors=colors, shadow=lambda , startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.show()


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
# -*- coding: utf-8 -*-

'''
Created on 10th of March, 2014

@author: David K. Laundav
'''

# ===========================================================================
# IMPORTS
# ===========================================================================
from scipy import stats
from numpy import arange, poly1d, random
import matplotlib.pyplot as plt
from math import sqrt

# ===========================================================================
# DATA
# ----------------------------------
# Notes:
#     This is only example data, and should be substitued with your own
# ===========================================================================
x = arange(0, 9)
y = [int(20 * random.random()) for i in range(len(x))]

# ===========================================================================
# LINEAR REGRESSION
# ----------------------------------
# Notes:
#     alpha = the slope of the curve
#     beta = the point at which the slope intercepts at x = 0
#     r_value = the correlation coefficient
#     p_value = the p-value which the h0 hypothesis is tested against
#         In this case, a p-value of 0.0 would be a 100% match, indicating that the linear regression is perfectly aligned with the data points
#     std_err = the standard deviation
# ===========================================================================
alpha, beta, r_value, p_value, std_err = stats.linregress(x,
                                                          y)  # Use scipy to calculate the variables of the least squares fit
polynomial = poly1d([alpha, beta])  # Calculate the polynomial least squares fit as: "y = ax * b"
line = polynomial(
    x)  # Returns an array containing the carry sum of "beta -/+ alpha" for each element in x (+ if the slope is positive, otherwise -)
sose = sqrt(sum((line - y) ** 2) / len(y))  # Calculate the Sum of Squared Errors

# ===========================================================================
# PLOTTING
# ===========================================================================
fig = plt.figure()
ax = fig.add_subplot(111)

""" Writing the variables to the plot """
text_string = "Alpha: %f" % (alpha)
text_string += "\nBeta: %f" % (beta)
text_string += "\nCorrelation coefficient: %f" % (r_value)
text_string += "\nP-value: %f" % (p_value)
text_string += "\nStandard deviation: %f" % (std_err)
text_string += "\nSum of squared error: %f" % (sose)
ax.text(0.010, 0.972, text_string, transform=ax.transAxes, verticalalignment='top', bbox=dict(facecolor='none', pad=10),
        fontsize=8)


ax.scatter(0, beta, color='red', label='Intercept')
ax.scatter(x, y, color='grey', label='Data')
ax.plot(line, color='blue', label='Linear Regression')
ax.legend(loc=1, fontsize=10)
plt.show()