import math
import matplotlib.pyplot as plt

# Input values
frequency = 900
transmit_power = 20
tx_gain = 2
rx_gain = 2

distances = [0.1, 0.5, 1, 2, 3, 5]
received_values = []

print("FSPL AND RECEIVED POWER")
print("------------------------")

for d in distances:

    fspl = 32.44 + 20 * math.log10(d) + 20 * math.log10(frequency)

    received_power = transmit_power + tx_gain + rx_gain - fspl

    received_values.append(received_power)

    print("Distance:", d, "km")
    print("FSPL:", round(fspl, 2), "dB")
    print("Received Power:", round(received_power, 2), "dBm")
    print("------------------------")

# Graph output
plt.plot(distances, received_values, marker='o')
plt.title("Received Power vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Received Power (dBm)")
plt.grid(True)
plt.show()
