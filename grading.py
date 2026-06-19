name=input("Enter Student Name")
maths=float(input("Enter Maths Marks"))
science=float(input("Enter Science Marks"))
telugu=float(input("Enter Telugu Marks"))
english=float(input("Enter English Marks"))
hindi=float(input("Enter Hindi Marks"))
social=float(input("Enter Social Marks"))
if maths<35 or science<35 or telugu<35 or english<35 or hindi<35 or social<35:
    print("Result: Failed")
else:
    total=maths+science+telugu+english+hindi+social
    percentage=(total/600)*100
    if percentage>=90:
        print("A+ Grade")
    elif percenatge>=80:
        print("A Grade")
    elif percentage>=70:
        print("B+ Grade")
    elif percedntage>=60:
        print("B Grade")
    elif percentage>=50:
        print("C Grade")
    else:
        print("D Grade")
    print("Percentage is: ",percentage)
    print("Result: Passed")