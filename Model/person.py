from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    name: str
    age: int
    height: float  # in meters
    weight: float  # in kilograms
    bmi: Optional[float] = None
    category: Optional[str] = None

    def calculate_bmi(self) -> float:
        """Calculate BMI using the formula: weight (kg) / (height (m))^2"""
        self.bmi = self.weight / (self.height ** 2)
        return self.bmi

    def get_bmi_category(self) -> str:
        """Get BMI category based on calculated BMI"""
        if self.bmi is None:
            self.calculate_bmi()
        
        if self.bmi < 18.5:
            self.category = "Gầy"
        elif 18.5 <= self.bmi < 25:
            self.category = "Bình thường"
        else:
            self.category = "Thừa cân"
            
        return self.category

    def __str__(self) -> str:
        """String representation of the person"""
        return f"{self.name} ({self.age} tuổi) - BMI: {self.bmi:.2f} - {self.category}"

