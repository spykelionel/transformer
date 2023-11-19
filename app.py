sn = ["C1", "c2", "c3", "c4", "c5", "c6"]
input = [
    "Overvoltages_network maneuvers",
    "Overvoltages_network maneuvers",
    ("Overvoltages_network maneuvers", "maneuvers_Proportion of each gaz",),
    "relocation of the transformer._Earthquake,_set of phase",
    "relocation of the transformer._Earthquake,_set of phase",
    "relocation of the transformer._Earthquake,_set of phase",
    ]

tools = [
    "Gas tight syringe Argon purges vials",
    "Gas_chromatography headspace sampling",
    "calculator",
    "Tester",
    "Smart sweep algorithm",
    "SFRAv6.2"
]

label = ["C1", "c2", "c3", "c4", "c5", "c6"]
cost = [10, 20, 3, 70, 5, 300]
component_or_step_objectif = [
    "Take the oil samples and fill into Argon purges vials",
    "Vials equilibrated by sample loop in HSS and inject into GC",
    "Check if the ratios ranges satisfy the Roger’s High energy electrical discharge ratio range",
    "Connect the transformer to the analyzer and measure the different primary and secondary voltages and calculate the corresponding ratios",
    "Calculate the gains and plot the SFRA test for the different phases. (gain as a function of frequencies)",
    "Detect the presence of failure"
]
duration = [10, 5, 2, 5, 600, 15]

criteria = [
    "Temperature above up 300deg C",
    "No air in the argon purge",
    "Roger_normal",
    "At least one of the situations satisfied and the frequency range available",
    "(Open Circuit/Close Circuit)",
    "List of voltages (primary and secondary) and list of ratios (very slot)",
]

personnel = ["Technicien", "Technicien", "Technicien", "Expert", "Technicien", "Expert"]

percentage_accuracy = [99, 97, 99.99, 95, 95, 95]

type = ["Simple", "Simple", "Simple", "Simple", "Simple","Simple"]

type_ouput = [
    "sample oil",
    "sample oil",
    "High energy electrical discharge with accuracy",
    "List of voltages (primary and secondary) and list of ratios (very slot)",
    "Graph",
    "The failt with precision"
]

origin = ["DGA", "DGA", "Roger's method", "SFRA", "SFRA","SFRA",]
