import numpy as np
import matplotlib.pyplot as plt

# Observation data
trials = np.arange(1, 9)
l1 = [0.20, 0.25, 0.15, 0.18, 0.22, 0.19, 0.24, 0.23]  # distances from CG (m)
l2 = [0.30, 0.35, 0.40, 0.42, 0.28, 0.37, 0.32, 0.29]  # distances from CG (m)
k = np.sqrt(np.array(l1) * np.array(l2))  # radius of gyration (m)

# Print Observation Table
print("Observation Table:")
print("{:<6} {:<10} {:<10} {:<10}".format("Trial", "l1 (m)", "l2 (m)", "k (m)"))
for i in range(len(trials)):
    print("{:<6} {:<10.3f} {:<10.3f} {:<10.3f}".format(trials[i], l1[i], l2[i], k[i]))

# Average radius of gyration
k_avg = np.mean(k)
print(f"\nAverage Radius of Gyration: {k_avg:.3f} m")

# Plot Observation Table
plt.figure(figsize=(10, 6))
plt.plot(trials, l1, marker='o', label="l1 (m)", color='blue')
plt.plot(trials, l2, marker='s', label="l2 (m)", color='green')
plt.plot(trials, k, marker='^', label="k (m)", color='red')
plt.axhline(k_avg, color='gray', linestyle='--', label=f"Average k = {k_avg:.3f} m")
plt.xlabel("Trial Number")
plt.ylabel("Length (m)")
plt.title("Observation of l1, l2, and k (Radius of Gyration)")
plt.legend()
plt.grid(True)
plt.show()

# Labeled Diagram of Bar Pendulum
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 0], [-0.5, 0.5], 'k-', lw=3, label="Bar Pendulum")  # bar pendulum
ax.plot(0, 0, 'ro', label="Center of Gravity (CG)")  # center of gravity
ax.text(0.05, -0.25, "l1", color='blue')
ax.text(0.05, 0.25, "l2", color='green')
ax.arrow(0, 0, 0, -0.25, head_width=0.05, head_length=0.05, fc='blue', ec='blue')  # l1 arrow
ax.arrow(0, 0, 0, 0.25, head_width=0.05, head_length=0.05, fc='green', ec='green')  # l2 arrow
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.set_title("Bar Pendulum with l1 and l2 Labeled")
ax.legend()
plt.grid(True)
plt.show()