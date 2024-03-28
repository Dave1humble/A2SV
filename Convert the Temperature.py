class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Fahrenheit = celsius * 1.80 + 32.00
        return [celsius + 273.15, Fahrenheit]
