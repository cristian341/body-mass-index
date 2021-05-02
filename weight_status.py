
def weight_status(bmi):
    if bmi <= 18.5:
        print(f"Your BMI is {bmi} and your weight status is underweight")
    elif bmi is 18.5<= bmi <= 24.9:
        print(f"Your BMI is {bmi} and your weight status is normal")
    elif 25 <= bmi <= 29.9:
        print(f"Your BMI is {bmi} and your weight status is overweight")
    elif 30 <= bmi < math.inf:
        print(f"Your BMI is {bmi} and your weight status is obese")
