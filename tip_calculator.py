# tip calculator
#Author : hajar1010
#description : a little program that asks the user to input the cost of a meal and the percentage of the tip they would like to tip and it outputs how much the user should tip.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d =d.strip().replace("$","")
    return  float(d)

def percent_to_float(p):
    p=p.replace("%","")
    return float(p)/100


main()
