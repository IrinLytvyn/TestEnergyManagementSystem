from abc import ABC, abstractmethod
from typing import List


class EnergyCalculation(ABC):
    @abstractmethod
    def energy_calculation(self):
        pass


class SolarPanel(EnergyCalculation):

    def __init__(self, area: int, efficiency: int):
        self.area = area
        self.efficiency = efficiency

    @classmethod
    def from_string(cls, parsed_string: List[str]) -> "SolarPanel":
        for i in range(1, len(parsed_string), 2):
            if parsed_string[i] == "Area":
                area = parsed_string[i + 1]
            elif parsed_string[i] == "Efficiency":
                efficiency = parsed_string[i + 1]
        return cls(int(area), int(efficiency))

    def energy_calculation(self) -> int:
        return self.area * self.efficiency * 15


class WindTurbine(EnergyCalculation):

    def __init__(self, height: int, wind_speed_average: int):
        self.height = height
        self.wind_speed_average = wind_speed_average

    @classmethod
    def from_string(cls, parsed_string: List[str]) -> "WindTurbine":
        for i in range(1, len(parsed_string), 2):
            if parsed_string[i] == "Height":
                height = parsed_string[i + 1]
            elif parsed_string[i] == "WindSpeedAverage":
                wind_speed_average = parsed_string[i + 1]
        return cls(int(height), int(wind_speed_average))

    def energy_calculation(self) -> int:
        return self.height * self.wind_speed_average * 150


class HydroPlant(EnergyCalculation):

    def __init__(self, flow_rate: int, drop: int):
        self.flow_rate = flow_rate
        self.drop = drop

    @classmethod
    def from_string(cls, parsed_string: List[str]) -> "HydroPlant":
        for i in range(1, len(parsed_string), 2):
            if parsed_string[i] == "FlowRate":
                flow_rate = parsed_string[i + 1]
            elif parsed_string[i] == "Drop":
                drop = parsed_string[i + 1]
        return cls(int(flow_rate), int(drop))

    def energy_calculation(self) -> int:
        return self.flow_rate * self.drop * 12


class EnergySource:
    def __init__(self, strategy: EnergyCalculation):
        self.strategy = strategy

    def get_annual_energy(self) -> str:
        return f"{self.strategy.__class__.__name__} AnnualEnergyOutput {self.strategy.energy_calculation()}"


def get_energy_source(input_string: str) -> EnergySource:
    parsed_string = input_string.split()
    strategy_type = parsed_string[0]

    if strategy_type == "SolarPanel":
        strategy_type = SolarPanel.from_string(parsed_string)

    elif strategy_type == "WindTurbine":
        strategy_type = WindTurbine.from_string(parsed_string)

    elif strategy_type == "HydroPlant":
        strategy_type = HydroPlant.from_string(parsed_string)

    else:
        raise ValueError("Unknown energy source type")

    return EnergySource(strategy_type)


if __name__ == '__main__':
    input_string = input("Enter data: ")

    energy_source = get_energy_source(input_string)
    print(energy_source.get_annual_energy())
