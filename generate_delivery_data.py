import pandas as pd
import numpy as np

# For reproducibility, it makes your random number generation predictable and repeatable,
# so it will always produce the same results.
np.random.seed(42)

n = 200

# Generate 'n' numbers between 'a' and 'b' in 2dp
distance_km = np.round(np.random.uniform(0.5, 50, n), 2)
bread_weight_kg = np.round(np.random.uniform(0.25, 5, n), 2)
delivery_time = np.random.choice(['morning', 'afternoon', 'evening'], n)
weather = np.random.choice(['clear', 'rainy', 'cloudy'], n)
traffic_level = np.random.choice(['low', 'medium', 'high'], n)

# Simple cost formula
# Base + (distance * 30) + (weight * 100) + traffic multiplier + weather adjustment + time slot
traffic_multiplier = {'low': 0, 'medium': 200, 'high': 400}
weather_adjustment = {'clear': 0, 'rainy': 150, 'cloudy': 80}
time_bonus = {'morning': 0, 'afternoon': 100, 'evening': 200}

costs = []
for i in range(n):
    base = 500
    cost = (
        base +
        distance_km[i] * 30 +
        bread_weight_kg[i] * 100 +
        traffic_multiplier[traffic_level[i]] +
        weather_adjustment[weather[i]] +
        time_bonus[delivery_time[i]] +
        np.random.normal(0, 50)  # some noise
    )
    costs.append(int(np.round(cost)))

data = pd.DataFrame({
    'distance_km': distance_km,
    'bread_weight_kg': bread_weight_kg,
    'delivery_time': delivery_time,
    'weather': weather,
    'traffic_level': traffic_level,
    'delivery_cost': costs
})

data.to_csv('bread_delivery_data.csv', index=False)
print('CSV generated: bread_delivery_data.csv')
