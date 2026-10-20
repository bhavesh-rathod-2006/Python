def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"


print(calculate_result(80))
print(calculate_result(20))
print(calculate_result(30, 25))