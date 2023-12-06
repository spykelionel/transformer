import csv
import random

num_rows = 1000
csv_file = 'random_data.csv'

value1_range = (1, 100)
value2_range = (1, 100)
categories = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Cost', 'Duration', 'Component_Objectif'])
    
    for _ in range(num_rows):
        value1 = random.randint(*value1_range)
        value2 = random.randint(*value2_range)
        
        # Randomly select unique categories for each row
        num_categories = random.randint(0, min(6, len(categories)))
        categories_list = random.sample(categories, num_categories)
        
        row = [value1, value2, categories_list]
        writer.writerow(row)