Explanation of Calculations:
• Solar Panel:
○ AnnualEnergyOutput = Area × Efficiency × 15
○ ResourceDepletionRate = 100 / Efficiency

• Wind Turbine:
○ AnnualEnergyOutput = Height × WindSpeedAverage × 150
○ ResourceDepletionRate = 1000 / (Height * WindSpeedAverage)

• Hydro Plant:
○ AnnualEnergyOutput = FlowRate × Drop × 12
○ ResourceDepletionRate = FlowRate / Drop

Bonus Points For:
• Tests
• Code that is easy to extend to add more energy sources
○ For example: “OffshoreWindTurbine Height 70 WindSpeedAverage 8 CorrosionFactor 0.2”
○ Where AnnualEnergyOutput = Height × WindSpeedAverage × 160 × (1 - CorrosionFactor)
And ResourceDepletionRate = 1200 / (Height * WindSpeedAverage * (1 - CorrosionFactor))