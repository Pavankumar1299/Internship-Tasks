def pass_fail(marks):
    if marks >= 40:
        return "PASS"
    else:
        return "FAIL"

marks = int(input("Enter marks: "))
print("Result: ", pass_fail(marks))