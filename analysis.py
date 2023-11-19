import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "sn": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "input": [
        "Overvoltages_network maneuvers",
        "Overvoltages_network maneuvers",
        ("Overvoltages_network maneuvers", "maneuvers_Proportion of each gaz",),
        "relocation of the transformer._Earthquake,_set of phase",
        "relocation of the transformer._Earthquake,_set of phase",
        "relocation of the transformer._Earthquake,_set of phase",
    ],
    "tools": [
        "Gas tight syringe Argon purges vials",
        "Gas_chromatography headspace sampling",
        "calculator",
        "Tester",
        "Smart sweep algorithm",
        "SFRAv6.2",
    ],
    "cost": [10, 20, 3, 70, 5, 300],
    "component_or_step_objectif": [
        "Take the oil samples and fill into Argon purges vials",
        "Vials equilibrated by sample loop in HSS and inject into GC",
        "Check if the ratios ranges satisfy the Roger’s High energy electrical discharge ratio range",
        "Connect the transformer to the analyzer and measure the different primary and secondary voltages and calculate the corresponding ratios",
        "Calculate the gains and plot the SFRA test for the different phases. (gain as a function of frequencies)",
        "Detect the presence of failure",
    ],
    "criteria": [
        "Temperature above up 300deg C",
        "No air in the argon purge",
        "Roger_normal",
        "At least one of the situations satisfied and the frequency range available",
        "(Open Circuit/Close Circuit)",
        "List of voltages (primary and secondary) and list of ratios (very slot)",
    ],
    "duration": [10, 5, 2, 5, 600, 15],
    "personnel": ["Technician", "Technician", "Technician", "Expert", "Technician", "Expert"],
    "percentage_accuracy": [99, 97, 99.99, 95, 95, 95],
    "type": ["Simple", "Simple", "Simple", "Simple", "Simple", "Simple"],
    "type_output": [
        "Sample oil",
        "Sample oil",
        "High energy electrical discharge with accuracy",
        "List of voltages (primary and secondary) and list of ratios (very slot)",
        "Graph",
        "The fault with precision",
    ],
    "origin": ["DGA", "DGA", "Roger's method", "SFRA", "SFRA", "SFRA"],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.countplot(x='personnel', data=df)
plt.title('Distribution of Personnel')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(x='tools', data=df, order=df['tools'].value_counts().index)
plt.title('Tool Usage Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='sn', y='duration', data=df, palette='viridis')
plt.title('Duration Analysis for Different Components')
plt.show()


plt.figure(figsize=(12, 8))
sns.barplot(x='sn', y='percentage_accuracy', data=df, palette='coolwarm')
plt.title('Percentage Accuracy Analysis for Different Components')
plt.show()
