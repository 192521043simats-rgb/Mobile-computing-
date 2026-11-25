
import math
import matplotlib.pyplot as plt

# Input values
traffic_values = [2, 5, 8, 10, 12, 15]
channels = 10

blocking_values = []

print("CALL BLOCKING PROBABILITY USING ERLANG B")
print("----------------------------------------")

for A in traffic_values:

    # Erlang B Formula
    B = 1.0

    for i in range(1, channels + 1):
        B = (A * B) / (i + A * B)

    blocking_probability = B * 100

    blocking_values.append(blocking_probability)

    print("Traffic Intensity:", A, "Erlangs")
    print("Number of Channels:", channels)
    print("Call Blocking Probability:",
          round(blocking_probability, 2), "%")
    print("----------------------------------------")

# Graph output
plt.plot(traffic_values, blocking_values, marker='o')
plt.title("Traffic Intensity vs Call Blocking Probability")
plt.xlabel("Traffic Intensity (Erlangs)")
plt.ylabel("Blocking Probability (%)")
plt.grid(True)
plt.show()
