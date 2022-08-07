#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

###########################

#UDEMY SOLUTION:
#password = ''
##nr_letters = 4
#for char in range(1, nr_letters + 1):
  #1-4
#  password += random.choice(letters)
  
#for char in range(1, nr_symbols + 1):
#  password += random.choice(symbols)

#for char in range(1, nr_numbers + 1):
#  password += random.choice(numbers)

##############  

#MY SOLUTION:
#ps_letters = random.sample(letters, nr_letters)
#ps_symbols = random.sample(symbols, nr_symbols)
#ps_numbers = random.sample(numbers, nr_numbers)

#print(''.join(ps_letters) + ''.join(ps_symbols) + ''.join(ps_numbers))

#or

#password = ''
#final_list = ps_letters + ps_symbols + ps_numbers

#for elements in final_list:
#  password += '' + elements  
#print(password)

############################

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#UDEMY SOLUTION:

#password = []
##nr_letters = 4
#for char in range(1, nr_letters + 1):
  #1-4
#  password += random.choice(letters)
  
#for char in range(1, nr_symbols + 1):
# password += random.choice(symbols)

#for char in range(1, nr_numbers + 1):
#  password += random.choice(numbers)

################################

#MY SOLUTION
ps_letters = random.sample(letters, nr_letters)
ps_symbols = random.sample(symbols, nr_symbols)
ps_numbers = random.sample(numbers, nr_numbers)

password = ''
final_list = ps_letters + ps_symbols + ps_numbers
random.shuffle(final_list)

for elements in final_list:
  password += '' + elements  
print(password)











  














  



  