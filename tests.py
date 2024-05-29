import unittest
from main import SolarPanel, WindTurbine, HydroPlant, EnergySource, get_energy_source


class TestSolarPanel(unittest.TestCase):

    def test_solar_panel(self):
        solar_panel = SolarPanel(20, 15)
        result = solar_panel.energy_calculation()
        self.assertEqual(result, 4500)

    def test_from_string(self):
        solar_panel = SolarPanel.from_string(["SolarPanel", "Area", "20", "Efficiency", "15"])
        result = solar_panel.energy_calculation()
        self.assertEqual(result, 4500)


class TestWindTurbine(unittest.TestCase):

    def test_wind_turbine(self):
        wind_turbine = WindTurbine(50, 6)
        result = wind_turbine.energy_calculation()
        self.assertEqual(result, 45000)

    def test_from_string(self):
        solar_panel = WindTurbine.from_string(["WindTurbine", "Height", "50", "WindSpeedAverage", "6"])
        result = solar_panel.energy_calculation()
        self.assertEqual(result, 45000)


class TestHydroPlant(unittest.TestCase):
    def test_hydro_plant(self):
        hydro_plant = HydroPlant(300, 20)
        result = hydro_plant.energy_calculation()
        self.assertEqual(result, 72000)

    def test_from_string(self):
        solar_panel = HydroPlant.from_string(["HydroPlant", "FlowRate", "300", "Drop", "20"])
        result = solar_panel.energy_calculation()
        self.assertEqual(result, 72000)

    @unittest.expectedFailure
    def test_from_string_not_all_argument(self):
        HydroPlant.from_string(["HydroPlant", "FlowRate", "10", "Drop"])

    @unittest.expectedFailure
    def test_from_string_bad_type(self):
        HydroPlant.from_string(["HydroPlant", "FlowRate", "one", "Drop", "20"])


class TestEnergySource(unittest.TestCase):

    def test_get_annual_energy(self):
        expected = "SolarPanel AnnualEnergyOutput 4500"
        energy_source = EnergySource(SolarPanel(20, 15))
        result = energy_source.get_annual_energy()
        self.assertEqual(result, expected)


class TestGetEnergySource(unittest.TestCase):

    def test_get_energy_source(self):
        result = get_energy_source("WindTurbine Height 50 WindSpeedAverage 6")
        self.assertTrue(isinstance(result, EnergySource))
        self.assertTrue(isinstance(result.strategy, WindTurbine))

    def test_get_energy_source_bad(self):
        with self.assertRaises(ValueError):
            get_energy_source("hello")
