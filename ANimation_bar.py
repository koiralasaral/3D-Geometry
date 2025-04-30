import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------
# Experimental Constants
# ---------------------
g = 9.81  # acceleration due to gravity (m/s^2)

# True value for radius of gyration (for simulation purpose)
k_true = 0.29  # m (typical for a uniform bar ~1 m long)

# ---------------------
# Synthetic Data Generation (Observation Table)
# ---------------------
# Define 8 different pivot distances (d from pivot to center of mass in m)
d_data = np.array([0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45])
n_trials = len(d_data)

# The model for the period: T = 2π * sqrt((k^2 + d^2) / (g * d))
def T_model_true(k, d):
    return 2 * np.pi * np.sqrt((k**2 + d**2) / (g * d))

# Generate true period values
T_true = T_model_true(k_true, d_data)

# Simulate measured periods with some random error (sigma = 0.02 s)
np.random.seed(42)
sigma = 0.02  # standard deviation of measurement noise
T_obs = T_true + np.random.normal(0, sigma, size=d_data.shape)

# Compute k for each trial using the rearranged formula:
# k = sqrt((T^2 * g * d)/(4π^2) - d^2)
computed_k = np.sqrt((T_obs**2 * g * d_data) / (4 * np.pi**2) - d_data**2)

# Print Observation Table
print("Observation Table:")
print("{:<6} {:<8} {:<10} {:<10}".format("Trial", "d (m)", "T_obs (s)", "Computed k (m)"))
for i in range(n_trials):
    print("{:<6} {:<8.3f} {:<10.3f} {:<10.3f}".format(i+1, d_data[i], T_obs[i], computed_k[i]))

# ---------------------
# MCMC Simulation to Estimate k
# ---------------------
# We use the likelihood function based on the period measurements:
# For each observation: T_obs[i] ~ Normal(T_model(k, d_i), sigma)
def T_model(k, d):
    return 2 * np.pi * np.sqrt((k**2 + d**2) / (g * d))

def log_likelihood(k):
    # Use uniform prior: k > 0 and k < 1 (m)
    if k <= 0 or k > 1:
        return -np.inf
    model = T_model(k, d_data)
    return -0.5 * np.sum(((T_obs - model) / sigma)**2)

# MCMC parameters
n_steps = 5000
proposal_std = 0.005  # proposal standard deviation
k_chain = np.zeros(n_steps)
k_current = 0.25  # initial guess
log_like_current = log_likelihood(k_current)

# MCMC loop (Metropolis-Hastings)
for i in range(n_steps):
    k_proposal = k_current + np.random.normal(0, proposal_std)
    log_like_proposal = log_likelihood(k_proposal)
    # Acceptance probability
    if np.random.rand() < np.exp(log_like_proposal - log_like_current):
        k_current = k_proposal
        log_like_current = log_like_proposal
    k_chain[i] = k_current

# Discard burn-in (first 1000 iterations)
burn_in = 1000
k_chain_post = k_chain[burn_in:]
k_est = np.mean(k_chain_post)
print(f"\nEstimated radius of gyration, k = {k_est:.3f} m (True k = {k_true:.3f} m)")

# ---------------------
# Plotting the MCMC Trace and Histogram
# ---------------------
fig, (ax_trace, ax_hist) = plt.subplots(2, 1, figsize=(8, 8))

# Trace plot
ax_trace.plot(k_chain, color="blue")
ax_trace.set_xlabel("Step")
ax_trace.set_ylabel("k (m)")
ax_trace.set_title("MCMC Trace for radius of gyration")

# Histogram for posterior
ax_hist.hist(k_chain_post, bins=30, density=True, color="green", alpha=0.7)
ax_hist.axvline(k_est, color="red", linestyle="--", label=f"Mean k = {k_est:.3f} m")
ax_hist.set_xlabel("k (m)")
ax_hist.set_ylabel("Probability Density")
ax_hist.set_title("Posterior Distribution of k")
ax_hist.legend()

plt.tight_layout()
plt.show()

# ---------------------
# Graph: Plot of T_obs vs d with model T(k_est, d)
# ---------------------
d_plot = np.linspace(0.08, 0.50, 200)
T_model_est = T_model(k_est, d_plot)

plt.figure(figsize=(8, 6))
plt.plot(d_plot, T_model_est, label="Fitted Model", color="blue")
plt.scatter(d_data, T_obs, color="red", zorder=5, label="Observed Data")
plt.xlabel("Pivot Distance d (m)")
plt.ylabel("Period T (s)")
plt.title("Period vs. Pivot Distance with Fitted Model")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------
# 3D Animation of the Bar Pendulum Experiment
# ---------------------
#
# For the animation, we simulate the swinging of a bar pendulum for one trial.
# We consider a bar of length L (assumed 1.0 m). The pivot is such that its 
# distance from the center-of-mass is d_animate.
# The angular motion is approximated by: θ(t) = θ_max * cos(ωt),
# where ω = sqrt(g*d/(k_est^2 + d^2)).
#
# The bar is represented as a line; knowing that the center-of-mass of 
# a uniform bar lies at L/2 from either end:
L = 1.0      # length of the bar (m)
d_animate = 0.30  # choose one pivot configuration (m)
theta_max = np.deg2rad(10)  # maximum angular displacement (10° in radians)
omega = np.sqrt(g * d_animate / (k_est**2 + d_animate**2))  # angular frequency

# The pivot (origin) is fixed. To compute the bar endpoints:
#
# 1. The center-of-mass (CM) of the bar is at a distance d_animate from the pivot, along the bar.
# 2. The bar makes an angle θ with the vertical. For small oscillations: θ(t)=theta_max*cos(omega*t).
# 3. If the pivot is at (0, 0), then the CM is:
#      x_cm = d_animate * sin(θ)
#      y_cm = -d_animate * cos(θ)
#
# 4. The bar extends a length of L/2 on either side of the CM along its axis. If we assume the bar is aligned
#    in the direction of θ, then the endpoints (x1,y1) and (x2,y2) are:
#      x1 = x_cm - (L/2)*cos(θ),  y1 = y_cm - (L/2)*sin(θ)
#      x2 = x_cm + (L/2)*cos(θ),  y2 = y_cm + (L/2)*sin(θ)

fig_anim, ax_anim = plt.subplots(figsize=(6, 6))
ax_anim.set_xlim(-1.2, 1.2)
ax_anim.set_ylim(-1.8, 0.5)
ax_anim.set_aspect('equal')
ax_anim.set_xlabel("X (m)")
ax_anim.set_ylabel("Y (m)")
ax_anim.set_title("Animation of Bar Pendulum Experiment")

line, = ax_anim.plot([], [], 'o-', lw=3, color='purple')  # pendulum (bar) representation
pivot_point, = ax_anim.plot(0, 0, 'ko', markersize=8)       # pivot

def init():
    line.set_data([], [])
    return line, pivot_point

def update(frame):
    t = frame / 30.0  # time in seconds (adjust frame rate as needed)
    theta = theta_max * np.cos(omega * t)
    
    # CM position
    x_cm = d_animate * np.sin(theta)
    y_cm = -d_animate * np.cos(theta)
    
    # Endpoints of the bar
    x1 = x_cm - (L/2)*np.cos(theta)
    y1 = y_cm - (L/2)*np.sin(theta)
    x2 = x_cm + (L/2)*np.cos(theta)
    y2 = y_cm + (L/2)*np.sin(theta)
    
    line.set_data([x1, x2], [y1, y2])
    return line, pivot_point

ani = FuncAnimation(fig_anim, update, frames=300, init_func=init, interval=33, blit=True)
plt.show()