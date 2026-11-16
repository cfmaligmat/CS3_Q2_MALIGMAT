# Realization:
from abc import ABC, abstractmethod


class IVehicle(ABC):
    
    @abstractmethod
    def start_engine(self) -> None:
        """All vehicles must implement this method."""
        pass


class Car(IVehicle):
    
    def start_engine(self) -> None:
        print("Engine started.")


if __name__ == "__main__":
    my_car = Car()
    my_car.start_engine() 


# Inheritance:
class Vehicle:
    def __init__(self):
        self.brand = "Generic"
        
    def move(self) -> None:
        print("Moving forward...")


class Car(Vehicle):
    def drive(self) -> None:
        self.move()  
        print("Car driving smoothly.")


my_car = Car()
my_car.drive()


# Association:
from __future__ import annotations
from typing import Optional


class Patient:

    def __init__(self, primary_doctor: Optional[Doctor] = None) -> None:
        self.primary_doctor = primary_doctor


class Doctor:
 
    def __init__(self, patients: Optional[list[Patient]] = None) -> None:
        self.patients = patients if patients is not None else []


# Aggregation:
from typing import Optional


class Wheel:

    pass


class Car:
   
    def __init__(self, wheels: Optional[list[Wheel]] = None) -> None:
        self._wheels = wheels if wheels is not None else []


# Composition:
class Engine:

    pass


class Car:
    def __init__(self) -> None:
        self._engine = Engine()


# Dependency:
class FormatUtility:
    def clean_text(self, input_str: str) -> str:
        return input_str.strip()


class ReportGenerator:

    def generate_report(self, utility: FormatUtility, raw_data: str) -> None:
        processed_data = utility.clean_text(raw_data)
        print(f"Report: {processed_data}")