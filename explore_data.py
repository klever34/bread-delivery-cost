import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bread_delivery_data.csv')

# Show the first 5 rows of the data
print(df.head())

print('\nInfo:')
print(df.info())

print('\nSummary stats:')
print(df.describe())

print('\nMissing values per column:')
print(df.isnull().sum())

# Plot the distribution of delivery distances
plt.hist(df['distance_km'], bins=30, edgecolor='green')
plt.xlabel('Distance (km)')
plt.ylabel('Number of Deliveries')
plt.title('Distribution of Delivery Distances')
plt.show()


# Distance vs Delivery Cost
plt.scatter(df['distance_km'], df['delivery_cost'])
plt.xlabel('Distance (km)')
plt.ylabel('Delivery Cost')
plt.title('Delivery Cost vs Distance')
plt.show()

# Bread Weight vs Delivery Cost
plt.scatter(df['bread_weight_kg'], df['delivery_cost'])
plt.xlabel('Bread Weight (kg)')
plt.ylabel('Delivery Cost')
plt.title('Delivery Cost vs Bread Weight')
plt.show()

print('\nAverage delivery cost by traffic level:')
print(df.groupby('traffic_level')['delivery_cost'].mean())

