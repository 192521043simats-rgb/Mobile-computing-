
import math
import matplotlib.pyplot as plt

# Input values
total_channels = 280
cell_radius = 1
reuse_factor = [3, 4, 7, 9, 12]

received_values = []
capacity_values = []

print("FREQUENCY (CO-CHANNEL) REUSE")
print("----------------------------")

for N in reuse_factor:

    cluster_size = N

    channels_per_cell = total_channels / cluster_size

    reuse_ratio = math.sqrt(3 * cluster_size)

    q = reuse_ratio

    S_I = (q ** 4) / 6

    S_I_dB = 10 * math.log10(S_I)

    capacity_values.append(channels_per_cell)
    received_values.append(S_I_dB)

    print("Cluster Size:", cluster_size)
    print("Reuse Ratio (Q):", round(reuse_ratio, 2))
    print("Channels per Cell:", round(channels_per_cell, 2))
    print("S/I Ratio:", round(S_I, 2))
    print("S/I in dB:", round(S_I_dB, 2), "dB")
    print("----------------------------")

plt.plot(reuse_factor, capacity_values, marker='o')
plt.title("Cluster Size vs Channel Capacity")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Channels per Cell")
plt.grid(True)
plt.show()

plt.plot(reuse_factor, received_values, marker='o')
plt.title("Cluster Size vs S/I Ratio")
plt.xlabel("Cluster Size (N)")
plt.ylabel("S/I Ratio (dB)")
plt.grid(True)
plt.show()
