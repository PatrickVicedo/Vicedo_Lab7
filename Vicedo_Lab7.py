name = input("Enter Your Name: ")
section = input("Enter Your Section: ")

prelims = float(input("Enter Your Prelims Grade: "))
if prelims < 40 or prelims > 100:
    print("Invalid Prelims Grade. Please Enter a Grade between 40 and 100.")
else:
    midterms = float(input("Enter Your Midterms Grade: "))
    if midterms < 40 or midterms > 100:
        print("Invalid Midterms Grade. Please Enter a Grade between 40 and 100.")
    else:
        finals = float(input("Enter Your Finals Grade: "))
        if finals < 40 or finals > 100:
            print("Invalid Finals Grade. Please Enter a Grade between 40 and 100.")
        else:
            prelims2 = prelims * 0.3333
            midterms2 = midterms * 0.3333
            finals2 = finals * 0.3333

            final_grade = prelims2 + midterms2 + finals2
            compute = round(final_grade)

         
if compute >= 99 and compute <= 100:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 1.00!")

elif compute >= 96 and compute <= 98:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 1.25!")

elif compute >= 93 and compute <= 95:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 1.50!")

elif compute >= 90 and compute <= 92:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 1.75!")

elif compute >= 87 and compute <= 89:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 2.00!")

elif compute >= 84 and compute <= 86:  
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 2.25!")

elif compute >= 81 and compute <= 83:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 2.50!")

elif compute >= 78 and compute <= 80:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 2.75!")

elif compute >= 75 and compute <= 77:
    print("Congratulations,", name, "your weighted Final Grade is", compute, "and your GPA is 3.00!")
    
else: 
    print("Do better next time,", name, "your weighted Final Grade is", compute, "and your GPA is 5.00")




