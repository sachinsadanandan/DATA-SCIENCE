import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
plt.plot(iris.Id, iris["SepalLengthCm"], "r--")
plt.show