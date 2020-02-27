import matplotlib.pyplot as plt

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='navy', alpha=0.5)
plt.ylabel("Frequencia")
plt.xlabel("idade")
plt.title("Idade da população de  um País")
plt.show()