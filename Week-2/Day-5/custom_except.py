class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError("Age must be 18 or above")
    print("Access granted")

except AgeTooSmallError as e:
    print("Custom Error:", e)

finally:
    print("custom excepts are defined in new class, extends the main 'Exception' calss "
    "\nand throwed using 'raise' keyword")