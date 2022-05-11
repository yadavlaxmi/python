#33. Write function bmi that calculates body mass index (bmi = weight / height2).

#if bmi > 30 return "Obese"
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"

def fun():
    a=int(input("weight"))
    height=2
    bmi=a/height
    if a>30:
        print("obese")
    if a<=18.5:
        print("underweight")
    if a<=25.0:
        print("normal")
    if a<=30:
        print("overweight")
fun()
    