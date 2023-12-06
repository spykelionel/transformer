import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)  # Set seed for reproducibility

num_rows = 1000
cost_values = np.random.randint(20, 100, size=num_rows)
duration_values = np.random.randint(1, 100, size=num_rows)

# Ensure unique tuples for Component_Objectif
component_objectif_values = [
    tuple(np.unique(np.random.choice(['C1', 'C2', 'C3', 'C4', 'C5', 'C6'], size=np.random.randint(0, 4))))
    for _ in range(num_rows)
]

# Convert tuples to lists
component_objectif_values = [list(components) for components in component_objectif_values]

# Create a DataFrame
data = pd.DataFrame({
    'Cost': cost_values,
    'Duration': duration_values,
    'Component_Objectif': component_objectif_values
})

# Save to CSV
data.to_csv('data.csv', index=False)

print("Random data saved to 'data.csv'")
