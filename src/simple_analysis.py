import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(100)

sns.histplot(data, kde=True)
plt.title("Sample Distribution with Seaborn")
plt.show()
