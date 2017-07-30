i=10

try:
    j=i/0
    print(j)

except Exception as e:
    print("exception found by python interpreter is:=>", e)
    print("Error.")
    
finally:
    print("finally executed")
