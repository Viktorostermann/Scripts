from abc import ABC, abstractmethod

# Interface

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def set_temperature(self) -> None:
        pass

# SubClases que implementan la interface SmartDevice

class SmartLight(SmartDevice):
    def turn_on(self) -> None:
        print(f"Turning on the smart light.")


    def turn_off(self) -> None:
        print(f"Turning off the smart light.")


 # Este metodo es el que no permite cumplir con el principio de segregación de interfaces
    def set_temperature(self, temperature: int) -> None:
        raise NotImplementedError("SmartLight does not support setting temperature.")


class SmartThermostat(SmartDevice):
    def turn_on(self) -> None:
        print(f"Turning on temperature of the smart thermostat ON.")

    def turn_off(self) -> None:
        print(f"Turning off the smart thermostat OFF.")

# Uso de las clases

light = SmartLight()
light.turn_on()
light.turn_off()
# light.set_temperature()

thermostat = SmartThermostat()
thermostat.turn_on()
thermostat.turn_off()
thermostat.set_temperature(10)
