class DataDTO:
    def __init__(self):
        self.gender = 0.0
        self.age = 0.0
        self.hypertension = 0.0
        self.heart_disease = 0.0
        self.smoking = 0.0
        self.bmi = 0.0
        self.diabetes = 0.0
        self.fast = 0.0
        self.carbohydrates = 0.0

    def set_gender(self, gender: float):
        self.gender = gender
        return self

    def set_age(self, age: float):
        self.age = age
        return self

    def set_hypertension(self, hypertension: float):
        self.hypertension = hypertension
        return self

    def set_heart_disease(self, heart_disease: float):
        self.heart_disease = heart_disease
        return self

    def set_smoking(self, smoking: float):
        self.smoking = smoking
        return self

    def set_bmi(self, bmi: float):
        self.bmi = bmi
        return self

    def set_diabetes(self, diabetes: float):
        self.diabetes = diabetes
        return self

    def set_fast(self, fast: float):
        self.fast = fast
        return self

    def set_carbohydrates(self, carbohydrates: float):
        self.carbohydrates = carbohydrates
        return self

    def to_array(self):
        return [
            self.gender,
            self.age,
            self.hypertension,
            self.heart_disease,
            self.smoking,
            self.bmi,
            self.diabetes,
            self.fast,
            self.carbohydrates
        ]
