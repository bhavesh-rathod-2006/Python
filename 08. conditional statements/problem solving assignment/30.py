student_age=int(input("Enter student "))
marks=int(input("Enter your exam's marks "))
family_income=int(input("Enter your family income "))
Attendance_percentage=int(input("Enter your attendance percentage "))

if 18<=student_age<=25 and marks>=85  and Attendance_percentage>=75 and family_income<=300000:
    print("scholarship Approved ")
    
elif 18>student_age>25 :
    print("Scholarship rejected \n because age factor is not satisfie ")

elif marks<85 :
    print("Scholarship rejected \n because marks factor is not satisfie ")

elif Attendance_percentage<75:
    print("Scholarship rejected \n because Attendance factor is not satisfie ")  

else:
    print("Scholarship rejected \n because Family income factor is not satisfie ")


    




 