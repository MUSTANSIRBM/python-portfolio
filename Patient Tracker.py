class Patient:
    def __init__(self,name,weight,height):
        self.bmi = 0
        self.name = name
        self.weight = weight
        self.height = height
    def calculate_bmi(self):
        self.bmi = self.weight / (self.height *self.height)
        return self.bmi
    def __str__(self):
        return f'{self.name} - BMI :{self.bmi} {self.calculate_bmi()}'
class Clinic:
    def __init__(self):
        self.patients = []
        self.load_data()
    def add_patient(self, name, weight, height):
        bmi_of_p = Patient(name, weight, height)
        self.patients.append(bmi_of_p)
        self.save_data()
    def show_risk_patients(self):
        for p in self.patients:
            bmi = p.calculate_bmi()
            print(bmi)

            if bmi > 25:
                print(f'{p.name} is Overweight (BMI: [{round(bmi)}])')
            elif bmi < 18.5:
                print(f'{p.name} is Underweight (BMI: [{round(bmi)}])')
    def save_data(self):
        with open('patients.txt','w') as f:
            for p in self.patients:
                f.write(f'{p.name} {p.weight} {p.height}\n')
    def load_data(self):
        try:
            with open('patients.txt', 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    parts = line.split(',')
                    if len(parts) == 3:
                        name_str, weight_str, height_str = parts
                        w = float(weight_str)
                        h = float(height_str)
                        loaded = Patient(name_str, w, h)
                        self.patients.append(loaded)
        except FileNotFoundError:
            pass
clinic = Clinic()
clinic.add_patient("Alice", 60.0, 1.65) # Normal
clinic.add_patient("Bob", 90.0, 1.75)   # Overweight (BMI ~29)
clinic.add_patient("Charlie", 50.0, 1.80) # Underweight (BMI ~15)

print("\n--- Risk Report ---")
clinic.show_risk_patients()