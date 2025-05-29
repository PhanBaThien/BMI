from typing import Dict, Tuple
from Model.person import Person

class BMIService:
    # BMI Categories with their ranges
    BMI_CATEGORIES: Dict[str, Tuple[float, float]] = {
        "Gầy": (0, 18.4),
        "Bình thường": (18.5, 24.9),
        "Thừa cân": (25.0, 29.9),
        "Béo phì": (30.0, float('inf'))
    }

    @classmethod
    def calculate_bmi(cls, person: Person) -> float:
        """Calculate BMI for a person"""
        return person.calculate_bmi()

    @classmethod
    def classify_bmi(cls, person: Person) -> str:
        """Classify BMI into categories"""
        bmi = person.calculate_bmi()
        for category, (min_bmi, max_bmi) in cls.BMI_CATEGORIES.items():
            if min_bmi <= bmi <= max_bmi:
                return category
        return "Không xác định"

    @classmethod
    def get_bmi_advice(cls, person: Person) -> str:
        """Get health advice based on BMI category"""
        category = cls.classify_bmi(person)
        advice = {
            "Gầy": "Bạn nên tăng cường dinh dưỡng và tập luyện để tăng cân.",
            "Bình thường": "Bạn đang có chỉ số BMI khỏe mạnh. Hãy duy trì lối sống lành mạnh.",
            "Thừa cân": "Bạn nên có chế độ ăn uống hợp lý và tăng cường vận động.",
            "Béo phì": "Bạn nên tham khảo ý kiến bác sĩ và có kế hoạch giảm cân an toàn.",
            "Không xác định": "Không thể đưa ra lời khuyên với chỉ số BMI này."
        }
        return advice.get(category, "Không có lời khuyên")
