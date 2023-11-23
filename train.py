import itertools

labels = ["C1", "C2", "C3", "C4", "C5", "C6"]

component_objectives = [
    "Take the oil samples and fill into Argon purges vials",
    "Vials equilibrated by sample loop in HSS and inject into GC",
    "Check if the ratios ranges satisfy the Roger’s High energy electrical discharge ratio range",
    "Connect the transformer to the analyzer and measure the different primary and secondary voltages and calculate the corresponding ratios",  
    "Calculate the gains and plot the SFRA test for the different phases. (gain as a function of frequencies)",
    "Detect the presence of failure"
]  

costs = [10, 20, 3, 70, 5, 300]

durations = [10, 5, 2, 5, 600, 15]

overvoltage_values = [0, 1]

sequences = list(itertools.product(overvoltage_values, repeat=len(labels)))

training_data = []

for seq in sequences:
    overvoltage = 1 if 1 in seq else 0
    
    input_data = {
        "Overvoltage": overvoltage,
        "Cost": sum([costs[i] for i in range(len(labels)) if seq[i] == 1]),
        "Duration": sum([durations[i] for i in range(len(labels)) if seq[i] == 1])
    }
    
    selected_index = next((i for i, value in enumerate(seq) if value == 1), None)
    output_data = {}
    if selected_index is not None:
        output_data = {
            "Component_Objective": component_objectives[selected_index]
        }

    training_data.append({**input_data, **output_data})
        
# Display training sets 
for data in training_data:
    print(data)