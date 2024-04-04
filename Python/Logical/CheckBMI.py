height=input("Enter You Height in Feet\n")
weight=input("Enter your weight in Kg\n")
Height_meter=float(height)*0.3048;
result=float(weight)/float(Height_meter ** 2)
int_Result=int(result)
print("Your BMI is\n "+str(int_Result))

