# Intro
A process for diagnosing potential issues with a transformer using dissolved gas analysis (DGA) and sweep frequency response analysis (SFRA). Here is my interpretation:

## There are 6 main steps (C1 to C6).
- C1/C2 involve taking oil samples from the transformer and analyzing them using gas chromatography to detect fault gases.
- C3 uses the DGA results and checks them against predefined "normal" ratios to detect abnormal conditions.
- C4/C5 involve doing SFRA testing by applying voltage sweeps and measuring frequency response. This can detect mechanical problems.
- C6 uses the SFRA results to precisely detect any faults present in the transformer.

In other words
- There are 6 steps involved in the diagnostic process (C1 to C6)
- These steps can be arranged in any order to create different permutations
- The goal is to find the permutation that maximizes accuracy while keeping the cost close to a target
- Each step has defined inputs, tools, objectives, criteria, duration, etc.
- By rearranging the order of the steps, different permutations are generated
- Certain orders may produce higher accuracy or lower costs than others
- An optimization approach is likely needed to search the permutation space and find the ideal sequence
- Constraints like total cost and minimum accuracy thresholds need to be considered

For each step, there are inputs, tools/components used, objectives, criteria to check, duration, personnel required, expected accuracy, output type, and origin of the data.

The overall goal seems to be detecting faults in a transformer using DGA and SFRA in a systematic way. The accuracy and costs associated with each step are provided as criteria.


| Node | Duration | Personnel              | Accuracy | Type   | Type Output                                                     | Origin                                                    |
|------|----------|------------------------|----------|--------|-----------------------------------------------------------------|-----------------------------------------------------------|
| C1   | 10       | Technician             | 99       | Simple | Sample oil                                                      | DGA                                                       |
| C2   | 20       | Technician             | 97       | Simple | Sample oil                                                      | DGA                                                       |
| C3   | 0        | Expert                 | 95       | Simple | List of voltages (primary and secondary) and list of ratios     | SFRA                                                      |
| C4   | 70       | Tester                 |          |        | the relocation of transformer. Earthquake, set of phase         | the relocation of transformer. Earthquake, set of phase |
| C5   | 5        | Smart sweep algorithm  |          |        | the relocation of transformer. Earthquake, set of phase         | the relocation of transformer. Earthquake, set of phase |
| C6   | 30       | Expert                 | 95       | Simple | Graph                                                           | SFRA                                                      |


# Complete table
| Component (step) | Input | Tools | Objective | Criteria | Duration | Cost | Personnel | Accuracy | Type | Type output | Origin | Sn |
|-|-|-|-|-|-|-|-|-|-|-|-|-|  
| C1 | Overvoltages_network maneuvers | Gas tight syringe Argon purges vials | Take the oil samples and fill into Argon purges vials | temperature above up 300° C. | 10 | ? | Technician | 99% | Simple | Sample oil | DGA |  |
| C2 | overvoltages,_network maneuvers Gas_chromatography headspace sampling | 20 Vials equilibrated by sample loop in HSS and inject into GC | No air in the argon purge | 5 | ? | Technician | 97% | simple | Sample oil | Dga | |
| C3 | overvoltages,_network maneuvers_Proportion of each gaz. | Calculator | 3 Check if the ratios ranges satisfy the Roger’s High energy electrical discharge ratio range | Roger_normal | 2 | ? | Technician | 99.99% | simple | High energy electrical discharge with acurracy | Roger’s method | |
| C4 | relocation of the transformer._Earthquake,_set of phase | Tester 70 Connect the transformer to the analyzer and measure the different primary and secondary voltages and calculate the corresponding ratios | At least one of the situations satisfied and the frequency range available | 5 | ? | Expert | 95% | Simple | List of voltages (primary and secondary) and list of ratios | SFRA | | 
| C5 | relocation of the transformer._Earthquake_set of phase | Smart sweep algorithm | 5 Calculate the gains and plot the SFRA test for the different phases. (gain as a function of frequencies) (Open Circuit/Close Circuit) | 600 | ? | Technician | 95% | Simple | Graph SFRA | SFRA | |
| C6 | relocation of the transformer._earthquake_set of phase | SFRAv6.2 | 300 Detect the presence of failure | List of voltages (primary and secondary) and list of ratios (very slow) | 15 | ? | Expert | 95% | Simple | The fault with precision. | SFRA | |