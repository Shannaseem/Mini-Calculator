#--------------taking the input form user--------
name = input("Enter your name: ")

while len(name) < 3:
    name = input("Enter correct spelling of your name (at least 3 characters): ")

print(f"Welcome, {name}")
print("This is Mini Calculator with History Feature")

def calculation():
    global out
    valid_operators=["+","-","*","/","%","**"]
    print("---------Mini Calculator With History--------- ")
    a=float(input("Enter the First Value : "))
    while True:
        op = input("Enter the operator (+, -, *, /, %, **) : ")
        if op in valid_operators:
          break
        else:
           print(" Invalid operator! Please enter again.")
    b=float(input("Enter the second Value : "))
    match op:
     case "+":
        print(f"Result : {a} + {b} = {a+b}")
        out=f"{a} + {b} = {a+b}"
        s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
        if s=="y":
            veiw_calculation.append(out)
        ask()
     case "-":
        print(f"Result : {a} - {b} = {a-b}")
        out=f"{a} - {b} = {a-b}"
        s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
        if s=="y":
            veiw_calculation.append(out)        
        ask()
     case "*":
        print(f"Result : {a} * {b} = {a*b}")
        out=f"{a} * {b} = {a*b}"
        s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
        if s=="y":
            veiw_calculation.append(out)        
        ask()
     case "/":
        if b==0:
           print("dividing a number by zero is not possible")
        else:
           print(f"Result : {a} / {b} = {a/b}")
           out=f"{a} / {b} = {a/b}"
           s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
        if s=="y":
            veiw_calculation.append(out)        
        ask()
     case "%":
         print(f"Result : {a} % {b} = {a%b}")
         out=f"{a} % {b} = {a%b}"
         s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
         if s=="y":
             veiw_calculation.append(out)       
         ask()
     case "**":
         print(f"Result : {a} ** {b} = {a**b}")
         out=f"{a} ** {b} = {a**b}"
         s=input("Press 'Y' to save this calculation, or 'N' to skip saving it.".lower())
         if s=="y":
            veiw_calculation.append(out)
         ask()
     case _:
         print("you enter the wrong operator")
         ask()
veiw_calculation=[]
def ask():
   print("-----------Do you want to----------- ")
   print("1: New Calculation")
   print("2: Veiw History ")
   print("3: Delete History")
   print("4: Exist")
   tell=input("Enter your choice : ")
   match tell:
      case "1":
        calculation()
      case "2":
        if veiw_calculation:
           print("\n--- Calculation History ---")
           index=1
           for x in veiw_calculation:
                
                print(index,": ",x)
                index+=1
        else:
            print("you donot have calculation history ")
        ask()
      case "3":
        if veiw_calculation:
           veiw_calculation.clear()
           print(veiw_calculation)
           print(" Your calculation history is clearing ")
        else:
           print("you donot have history to be clear")
        ask()
      case "4":
           print(f"{name}, Thanks for using Mini Calculator with History ")
           exit()
ask()    
      