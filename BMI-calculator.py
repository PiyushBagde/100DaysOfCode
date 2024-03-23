print('Welcome to BMI calculator')

weight = int(input("Enter your weight(Kgs): "))
Height = float(input("Enter your height(cm): "))

BMI = weight / ((Height*0.01)**2)

print(f'Your BMI is {BMI}.')
