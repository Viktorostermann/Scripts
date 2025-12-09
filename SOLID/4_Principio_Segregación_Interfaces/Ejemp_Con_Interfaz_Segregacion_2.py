from abc import ABC, abstractmethod

# Interface

class ISmartDeviceSwichable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass
    @abstractmethod
    def turn_off(self) -> None:
        pass


class ISmartDeviceTemperature(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int) -> None:
        pass

class ISmartLight(ISmartDeviceSwichable):
    def turn_on(self) -> None:
        print(f"Turning on the smart light.")
    def turn_off(self) -> None:
        print(f"Turning off the smart light.")

class ISmartThermostat(ISmartDeviceSwichable, ISmartDeviceTemperature):
    def turn_on(self) -> None:
        print(f"Turning on temperature of the smart thermostat ON.")
    def turn_off(self) -> None:
        print(f"Turning off the smart thermostat OFF.")
    def set_temperature(self, temperature: int) -> None:
        #return super().set_temperature(temperature)
        print(f"Setting temperature of the smart thermostat to {temperature} degrees.")

    # Uso de las clases
light = ISmartLight()
light.turn_on()
light.turn_off()


thermostat = ISmartThermostat()
thermostat.turn_on()
thermostat.turn_off()
thermostat.set_temperature(10)
