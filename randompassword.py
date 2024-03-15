import random
uppercase=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase=("abcdefghijklmnopqrstuvwxyz")
digits=("0123456789")
symbol=("@!#%*?/")
string=uppercase+lowercase+digits+symbol
length=int(input("Enter the length of password:"))
password="".join(random.sample(string,length))    
print("The Generated Password is:",password)
