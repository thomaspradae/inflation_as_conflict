import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_periods = 100  # Number of time periods
initial_prices = [1, 1]  # Initial nominal prices for goods A and B
elasticity = 1.5  # Elasticity of demand

# Utility function (can be adjusted)
def utility(c, c_prime):
    return np.log(c) + np.log(c_prime)

# Agent A price-setting function
def set_price_A(p_B, u_c, u_c_prime):
    return (1 / (1 - 1 / elasticity)) * (u_c / u_c_prime) * p_B

# Agent B price-setting function
def set_price_B(p_A, u_c, u_c_prime):
    return (1 / (1 - 1 / elasticity)) * (u_c / u_c_prime) * p_A

# Simulation
prices = np.zeros((n_periods, 2))  # Store prices for each period
prices[0] = initial_prices

for t in range(1, n_periods):
    if t % 2 == 0:  # Agent A sets price
        u_c, u_c_prime = 1, 1  # Simplified marginal utilities
        prices[t, 0] = set_price_A(prices[t - 1, 1], u_c, u_c_prime)
        prices[t, 1] = prices[t - 1, 1]  # B's price remains the same
    else:  # Agent B sets price
        u_c, u_c_prime = 1, 1  # Simplified marginal utilities
        prices[t, 1] = set_price_B(prices[t - 1, 0], u_c, u_c_prime)
        prices[t, 0] = prices[t - 1, 0]  # A's price remains the same

# Calculate inflation rate
inflation = np.diff(np.mean(prices, axis=1)) / np.mean(prices[:-1], axis=1)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(prices[:, 0], label="Price A")
plt.plot(prices[:, 1], label="Price B")
plt.title("Price Dynamics")
plt.xlabel("Periods")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(inflation, label="Inflation Rate")
plt.title("Inflation Over Time")
plt.xlabel("Periods")
plt.ylabel("Inflation Rate")
plt.legend()
plt.grid()
plt.show()
