try:
    x = int(input("Enter a number: "))
    print(10 / x)

except:
    print("Something went wrong")
    
finally:
    print("'finally' block, which runs no matter what")