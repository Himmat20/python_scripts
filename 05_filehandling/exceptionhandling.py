# try
try:
    x=int(input("enter x:"))
    ans=10/x
except ZeroDivisionError:
    print("divide by zero is not allowed")

except ValueError:
    print(f"invalid input")

else:
    print(f"ans={ans}")

# built in exception to check  on w3sschool

finally:
    print("End of program")