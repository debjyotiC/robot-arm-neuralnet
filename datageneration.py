import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l_1 = l_2 = l_3 = 2  # in meters

q_1 = np.arange(0, 180, dtype=float)
q_2 = np.arange(-180, 0, dtype=float)
q_3 = np.arange(-90, 90, dtype=float)

x_e = l_1 * np.cos(q_1) + l_2 * np.cos(q_1 + q_2) + l_3 * np.cos(q_1 + q_2 + q_3)
y_e = l_1 * np.sin(q_1) + l_2 * np.sin(q_1 + q_2) + l_3 * np.sin(q_1 + q_2 + q_3)
theta_e = q_1 + q_2 + q_3

# save performance data
# values = {'Q_1': q_1, 'Q_2': q_2, 'Q_3': q_3, 'X_e': np.round(x_e, 2), 'Y_e': np.round(y_e, 2), 'Theta_e': theta_e}
# df_w = pd.DataFrame(values, columns=['Q_1', 'Q_2', 'Q_3', 'X_e', 'Y_e', 'Theta_e'])
# df_w.to_csv("data-set/ik-data.csv", index=None, header=True)


plt.scatter(x_e, y_e)
plt.grid(True)
plt.show()
