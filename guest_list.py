print ("======================WELCOME TO THE BIRTHDAY PARTY REGISTER=================")

def number_of_guests():
    total_guests = int(input("Enter number of guests:"))
    return total_guests
def individual_printout():
    for detail in Register[counter]:
        print( detail,  ":",  Register[counter][detail] )

def total_printout():
    for counter in Register.keys():
        print("Guest id" ,counter)
        individual_printout()
        print("\n")

counter = 1
Register = {}


num = number_of_guests()

for counter in range(1,num+1):
    Register[counter] = {}
    Register[counter]['name'] = input("what is your name?: ")
    Register[counter]['gift'] = input("what gift have you brought for the host?")
    Register[counter]['gender'] = input("what is your gender?")
    Register[counter]['number'] = int(input("what is your phone number?"))
    Register[counter]['date_of_birth'] = input("what is your date of birth?")
    individual_printout()
    print("\n")

print("\n")
print("THIS IS OUR GUEST LIST PRINT OUT")
print ("====================================================================")

total_printout()

print ("====================================================================")

