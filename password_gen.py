import string
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3= string.punctuation
s4=string.digits
plen =int(input("Enter your password len "))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print("Your password is")
print("".join(s[0:plen]))