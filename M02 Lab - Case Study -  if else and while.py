#Name: Omonode Theodore
#App Name: Dean's list and Honor Roll App
#THis App will accept student names and GPAs and test if the student qualifies for either the Dean's list or the Honor Roll.

# This will run forever until we break it
#Testing the loop condtions
while True:

	student_last_name = input ("Enter your last name: ")    #Prompt user to enter Last name

	student_first_name = input ("Enter your first name: " ) #Prompt user to enter First name

	GPA = float(input("Enter you GPA: "))                   #Promt user to enter GPA

	if student_last_name == "zzz":                          # Check if last name Eqaul zzz if not (continue or break)
		break
                                                           
	if GPA >= 3.5 :                                         # Check if GPA is Equal 3.5 or Greater
                                                               
		print(student_last_name + ' ' + student_first_name + ' ' + "has made the Dean's List") #Print result

	elif GPA >=3.25 :                                       # Check if GPA is Equal 3.5 or Greater

		print(student_last_name + ' ' + student_first_name + ' ' + "has made the Honor Roll")   #Print result