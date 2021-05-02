import math
def bmi():
    def bmi_usa_uk(lbs,feet,inch): 
        weight_usa_uk = lbs * 0.4536
        height_usa_uk = feet*12
        height_usa_uk += inch
        height_usa_uk *= 0.0254
        bmi = round(weight_usa_uk/pow(height_usa_uk,2),2)
        if bmi <= 18.5:
            print(f"Your BMI is {bmi} and your weight status is underweight")
        elif  18.5<= bmi <= 24.9:
            print(f"Your BMI is {bmi} and your weight status is normal")
        elif 25 <= bmi <= 29.9:
            print(f"Your BMI is {bmi} and your weight status is overweight")
        elif 30 <= bmi < math.inf:
            print(f"Your BMI is {bmi} and your weight status is obese")

    def bmi_european(kg,m):
        m = m / 100
        bmi = round(kg / pow(m,2),2)
        if bmi <= 18.5:
            print(f"Your BMI is {bmi} and your weight status is underweight")
        elif  18.5<= bmi <= 24.9:
            print(f"Your BMI is {bmi} and your weight status is normal")
        elif 25 <= bmi <= 29.9:
            print(f"Your BMI is {bmi} and your weight status is overweight")
        elif 30 <= bmi < math.inf:
            print(f"Your BMI is {bmi} and your weight status is obese")

    print("""
For calculate your BMI, I need your weight and height:
Press 1 if your use USA/UK unit measure
Press 2 if you use European unit measure
""")   
    var = int(input("Enter what unit of measure you use:"))
    if var == int(1):
        lbs = float(input("Enter your weight in lbs: "))
        feet = float(input("Enter you height in feet: "))
        inch = float(input("Enter the inch:  "))
        bmi_usa_uk(lbs,feet,inch)
    elif var == int(2):
        kg = float(input("Enter your weight in kg: "))
        m = float(input("Enter your height in centimeters: "))
        bmi_european(kg,m)
    else:
        print("Try again:")

bmi()