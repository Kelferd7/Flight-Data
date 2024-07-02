import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the flight data
data = pd.read_csv('flightdata.csv', parse_dates=['timestamp'])

# Display the first few rows of the data
print(data.head())

# Set the timestamp as the index
data.set_index('timestamp', inplace=True)

# Plot altitude over time
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['altitude'], marker='o')
plt.title('Altitude Over Time')
plt.xlabel('Time')
plt.ylabel('Altitude (feet)')
plt.grid(True)
plt.show()

# Plot speed over time
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['speed'], marker='o', color='green')
plt.title('Speed Over Time')
plt.xlabel('Time')
plt.ylabel('Speed (knots)')
plt.grid(True)
plt.show()

# Plot fuel consumption over time
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['fuel_consumption'], marker='o', color='red')
plt.title('Fuel Consumption Over Time')
plt.xlabel('Time')
plt.ylabel('Fuel Consumption (kg)')
plt.grid(True)
plt.show()

# Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()
