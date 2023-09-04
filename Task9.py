#Q-1 find the expected output for below program
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x>4, data)
print(list(result))


#Q-2 check the element in the list is integer or string
def int_str(list_2):
    int_list_2 = list(filter(lambda z: type(z) == int, list_2))
    str_list_2 = list(filter(lambda z: type(z) == str, list_2))
   
    print("Integers in the Given list: ",int_list_2)
    print("strings in the Given list: ", str_list_2)

s2 = [10,25,'23.5','hello',56]
int_str(s2)



#Q-3 fibbonaci series for given number
def fibbi(q,n):
    fibboni = lambda n: n if n<=1 else fibboni(n-1) + fibboni(n-2)
    fibbi_series = list(map(fibboni, range(q, n+1)))

    if fibbi_series:
        return fibbi_series
    else:
        return "enter valid data"
s3 = int(input("Enter the Number for start limit fibbonacci: "))
s4 = int(input("Enter the Number for end limit fibbonacci: "))
print("Fibbonacci series for given number: ",fibbi(s3,s4))



#Q-4 Regrex pattern for given data
import re
def reg(email, ban_ph,us_land,alpha_pass):
    email_patt = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_patt, email):
        print(email, "is valid")
    else:
        print(email, "is not valid")


    ban_patt = r"^(?:\+?88)?\01[3-9]\d{8}$"
    if re.match(ban_patt, ban_ph):
        print("This ", ban_ph ,"Valid Bangladesh mobile number")
    else:
         print("This ", ban_ph ," is not a Valid Bangladesh mobile number")


    us_patt = r"^(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    if re.match(us_patt, us_land):
        print("This ", us_land ,"Valid USA landline number")
    else:
        print("This ", us_land ," is not a Valid USA landline number")
    

    pass_patt = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()-_+=])[A-Za-z0-9!@#$%^&*()-_+=]{16}$"
    if re.match(pass_patt, alpha_pass):
        print("This ", alpha_pass, "password is valid")
    else:
        print("This ", alpha_pass, "password is not valid")


e1 = input("Enter the email id: ")
b1 = input("Enter the bangladesh mobile number: ")
u1 = input("Enter the USA  landline number:")
p1 = input("Enter the 16aplha_numeric password:")
reg(e1,b1,u1,p1)