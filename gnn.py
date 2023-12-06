import numpy as np
import pandas as pd

# Function to generate random data
def generate_data(num_samples=100):
    np.random.seed(42)
    labels = ["C1", "C2", "C3", "C4", "C5", "C6"]
    
    # Generate random labels for Component_Step_Objectif
    data = {'Cost': np.random.randint(1, 100, size=num_samples),
            'Duration': np.random.randint(1, 100, size=num_samples),
            'Component_Step_Objectif': np.random.choice(labels, size=num_samples)}
    
    df = pd.DataFrame(data)
    return df

# Generate sample data
num_samples = 10000
sample_data = generate_data(num_samples)
sample_data.to_csv('transformer.csv', index=False)
# Display the generated sample data
# print(sample_data)
