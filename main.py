from abc import ABC, abstractmethod
from typing import List, Union


class EnergyCalculation(ABC):
    @abstractmethod
    def energy_calculation(self):
        pass

    @abstractmethod
    def resource_depletion_rate(self):
        pass

    @staticmethod
    def parse_property(parsed_string, property_name):
        for i in range(1, len(parsed_string), 2):
            if parsed_string[i] == property_name:
                value = parsed_string[i + 1]
        return value


class SolarPanel(EnergyCalculation):

    def __init__(self, area: int, efficiency: int):
        self.area = area
        self.efficiency = efficiency

    @classmethod
    def from_string(cls, parsed_string: List[str]) -> "SolarPanel":
        area = cls.parse_property(parsed_string, "Area")
        efficiency = cls.parse_property(parsed_string, "Efficiency")
        return cls(int(area), int(efficiency))

    def energy_calculation(self) -> int:
        return self.area * self.efficiency * 15

    def resource_depletion_rate(self) -> Union[float, int]:
        return 100 / self.efficiency


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

    def resource_depletion_rate(self) -> Union[float, int]:
        return 1000 / (self.height * self.wind_speed_average)


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

    def resource_depletion_rate(self) -> Union[float, int]:
        return self.flow_rate / self.drop


class OffshoreWindTurbine(WindTurbine):

    def __init__(self, height: float, wind_speed_average: float, corrosion_factor: float):
        super().__init__(height, wind_speed_average)
        self.corrosion_factor = corrosion_factor

    @classmethod
    def from_string(cls, parsed_string: List[str]) -> "OffshoreWindTurbine":
        wind_turbine = WindTurbine.from_string(parsed_string)
        for i in range(1, len(parsed_string), 2):
            if parsed_string[i] == "CorrosionFactor":
                corrosion_factor = parsed_string[i + 1]
        return cls(float(wind_turbine.height), float(wind_turbine.wind_speed_average), float(corrosion_factor))


class EnergySource:
    def __init__(self, strategy: EnergyCalculation):
        self.strategy = strategy

    def get_energy_source_details(self) -> str:
        return (
           f"{self.strategy.__class__.__name__} "
           f"AnnualEnergyOutput {self.strategy.energy_calculation()} "
           f"ResourceDepletionRate {round(self.strategy.resource_depletion_rate(), 2)}"
        )



def get_energy_source(input_string: str) -> EnergySource:
    parsed_string = input_string.split()
    strategy_type = parsed_string[0]

    if strategy_type == "SolarPanel":
        obj = SolarPanel.from_string(parsed_string)

    elif strategy_type == "WindTurbine":
        obj = WindTurbine.from_string(parsed_string)

    elif strategy_type == "HydroPlant":
        obj = HydroPlant.from_string(parsed_string)

    elif strategy_type == "OffshoreWindTurbine":
        obj = OffshoreWindTurbine.from_string(parsed_string)

    else:
        raise ValueError("Unknown energy source type")

    return EnergySource(obj)


if __name__ == '__main__':
    input_string = input("Enter data: ")

    energy_source = get_energy_source(input_string)
    print(energy_source.get_energy_source_details())
