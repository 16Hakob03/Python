                 #1
# a =float(input("Enter a="))
# print("fahrenheit =", a * 9//5 + 32)
                  
#                       #2
# a =float(input("Enter a="))
# print(("Celsius =", (a -32) * 5 ) /9)
#                     #3 

# minutes = int(input ("Enter minutes"))
# print ("Seconds = ", minutes * 60 )                    

                        #4
# Day = int (input("Nermucel oreri qanaky = ", ))
# print("1 ory ropenereov =", Day * 1440 ,"1 ory varkyannerov = " , Day * 86400)
                       #5
# a = float(input ('Enter a:  '))
# b = float(input ('Enter b:  '))
# a<90
# b<90
# c<=180
# print('c =', 180 - (a+b)) 



                         #6

# a = float(input("Nermucer arajin ankyan chapy: "))
# b = float(input("nermucel erkrord ankyan chapy: "))
 
# print ("Errord ankyan chapy= ", 180 - (a + b) ) 
                          
                            #7
# x = bool( input ("nermucel tvanshany", ))
# y =x > 100
# print (x) 

            #    ----------------------------------------------------
#
            #    x = input("Model").lower()
# y = input("Color").lower()
# z = ( x == "iphone12" and  y =="gold")
# print(z) ----------------------------------------------------
# a = int(input ('nermucel tivy :  '))
# print (a=>17 and =<27)

                  #    ----------------------------------------------------

# import random 
# x  = int(input ('nermucel  5 hat tiv :')) 
# print((random.randint) in x )

                  # ---------------------------------------------------------

# number = int(input('Enter number: '))
# print (number // 20 )


#----------------------------------------------------------------
# x = input("Model: ")
# y = input("taretiv: ")
# print(x =='M3' and y == '2022')
   

 #1----------------------------------------------------
# name = input("Enter your name: ")
# print('a' in name)

#2---------------------------- ------------------------
# name =input("grel mrgi anuny = ")

# print  ( name  in'banan ' or 'naring ' or 'xndzor'  )
#3--------------------------------------------------------
# x = float(input("nermucel arjeqy: "))

# print("Ardyunq 1:", x <= -8 or x > 12)
# print("Ardyunq 2:", x > 10 and x <= 50)
# print("Ardyunq 3:", x > -10 and x < 10)
# print("Ardyunq 4:", x != 20 or x > 50)
#---------------------------------------------------------------- 5
# import math
# x = float(input("nermucel arjeqy "))
# y = math.pi * x ** 2
# print ( f"x-i arjeqy =  {x} y-i arjeqy =  {y}")
#14 -> 20///////////////////////////////


# feet = float(input("nermucel 1-in arjeqy: "))
# inches = float(input("nermucer 2-rd arjeqy: "))
# x = 30.48
# y= 2.54

# z = (feet * x) + (inches * y)

# print(  "barcrutyuny cm-ov =", z)

#--------------------------------
# import math


# x = float(input("NErmucel sharavixy: "))

# y= math.pi * x ** 2
# z = (4 / 3) * math.pi *x ** 3

# print ("x =",y)
# print ("x =",z)
#//////////////////////////
# import math


# x = float(input("nermucel   arajin ajreqy    "))
# y = float(input("nermucel erkrord arjeqy "))

# print("z = ", (math.pi * x ** 2 * y))



#-------------------------------------------------
# import math
# x= float(input("Mutqagrel bardzrutyuny "))
# y = 9.8  
# print ('pataskhan =', math.sqrt(2 * y * x))



# R = 8.314  
# x = float(input("paskal "))
# y = float(input("litr "))
# z = float(input("jermastichan "))


# a = z + 273.15

# print ("pataskhan = ", x * y / (R * z))

#-------------------------------------------------------------
# import math


# x = float(input("nermucel arjeqy  "))

# print ( 'y =', math.pi * x ** 2)
# print ( 'z =', math.pi * x ** 3)



#---------------------------------------If else ------------------------------------------------------

# a = input('nermucel tary: ')
# b ='aeiou'
# if a in b:
#     print("dzaynavor")
# else:
#     print( "baxadzyan")


#100 -i u 400 //  4i bajanvuma  100-i che

# a =input ("nermucel tarin")
# if a % 4 == 0 and a  != 100 or a % 400 == 0:
#     print("nahanj")
#     else
#     print("+++")



# 1 ----------------------------------
# num1 = int(input("nermucel arajin tivy: "))
# num2 = int(input("Nermucel erkrord tivy: "))

# if num1 > num2:
#     print(f"Amenamec tivy  {num1}")
# elif num2 > num1:
#     print(f"Amrenamec tivy {num2}")
# else:
#     print("Erku tvern el havasar en ")
#2/////////////////////////////////////////////
# z = input("Enter a number: ")

# x = ""

# for y in z:
#     x = y + x

# print(f"patasxan =: {x}")
#3 -----------------------------
# l = input('Enter your position (LETTER):  ')
# n = input('Enter your position(NUMBER):  ')
# if l == ('a' or 'c' or 'e' or 'g') and (n == 1, 3, 5, 7):
#     print('black')
# elif l == ('a' or 'c' or 'e' or 'g') and (n == 2, 4, 6, 8):
#     print('white')
# elif l == ('b' or 'd' or 'f' or 'h') and (n == 1, 3, 5, 7):
#     print('white')
# else:
#     print('black')

# x= int(input("nermucel arajin tivy : "))
# y = int(input("nermucel erkrod tivy "))

# z = y * 1.20

# if x > z:
#     print("du bloger es.")
# else:
#     print("hamakrgichy bloger e .")
# a = int(input("enter number  1 "))
# b = int(input("enter number  2 "))
# for  i in range(1, a * b + 1 ):

#     if i % a == 0 and i% b ==0:
#         print (i)
#         break


#----------------------


#----------------------------
# for number in range(1, 101):
    
#     if number % 2 == 0:
    
#       print( len(str(number)))
#     else:
#      print("Number of odd numbers:" , number)

#----------------------------------------------------------------
# number = int(input("Grel tivy: "))

# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print( number, factorial)
#------------------------------------------------------------------
# x = int(input("Grir tariqd "))
# y = input("Txa es te axjik: ").strip().lower()


# if 18 >= x <= 20 and y == 'male':
#     print("18-20 txa es tesqov bari ")
# else:
#     print("Ches hamapatasxanum")
#-----------------------------------------------------------
# number = int (input("Enter number"))

# number2 = str(number)


# number3 = 0

# for digit in number2:
  
#     number3 += int(digit)

# print(number , number3)
#------------------------------------------------------
# x =4.95, 9.95, 14.95, 19.95, 24.95
# z = 0.60

# for price in x:
#     y= price * z
#     o = price - y
#     print(price ,y , o)
#----------------------------------------
# x = 0
# y = 0


# for number in range(1, 101):
#     if number % 2 == 0:
#          x += 1
#     else:
#        y+= 1


# print(x , y)


# number = 734215566


# number1 = len(str(number))


# print(number , number1)
#------------------------------------------------------------
# summ = 0
# count = 0
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     else:
#         summ += number
#         count += 1
# print(summ / count)

# #  3-14 14/ 65+ 18$ 12 65 23$
# # x =0
# # while True:
# #     number = int(input('Enter number:  '))
# #     if number == 0:
# #         break
# #     elif x< 3:
# #           x+=0


# # #------------------------
# # import random
# # x= 0
# # y=0
# # while True:
# #     z =random.choice("op")
# #     if x ==3 or y == 3:

# #         ##ցեզրի ալգորիթմ  ինչ տպես 3 ատռ առաջ պետքա տպի
# #         ##мутяа8ел бар  եթե նույն ձևա կարդացվում գրումա թռու
# #         #базмапаткман ажйшуска
# #         #81 10 -ic erkuakan 82




#73
# message = input("Մուտքագրեք հաղորդագրությունը: ")
# shift = int(input("Մուտքագրեք  չափը (կարող է լինել դրական կամ բացասական): "))


# result = ()


# for char in message:
#     if char.isalpha():

#         start = ord('A') if char.isupper() else ord('a')
      
#         new_char = chr((ord(char) - start + shift) % 26 + start)
#         result.append(new_char)
#     else:
#        result.append(char)


# shifted_message = ''.join(result)


# print("հաղորդագրությունը:", shifted_message)
#74---------------------------

# x = float(input("Մուտքագրեք թիվը "))
# if x < 0:
#     print("բացասական թիվ չի կարելի.")
# else:
    
#     guess = x / 2.0

    
#     y= 1e-12


#     while (guess * guess - x) > y:
#         guess = (guess + x / guess) / 2.0

#     print(x , guess)

#76------------------------------------------------------------------------
# input_string = input("Մուտքագրեք տողը՝ ստուգելու համար, թե արդյոք այն պալինդրոմ է: ")


# input_string = input_string.lower().replace(" ", "")


# palindrome = True
# length = len(input_string)
# i = 0
# while i < length // 2:
#     if input_string(i) != input_string(length - 1 - i):
#         is_palindrome = False
#         break
#     i += 1

# if is_palindrome:
#     print("Տողը պալինդրոմ է:")
# else:
#     print("Տողը պալինդրոմ չէ:")


#75-----------------------------------------------------
# for i in range(0, 6):

#     for j in range(0,11,2):
        

#         print (i, end=" ")
#     print ()
# n = int(input("Enter number"))
# if n%n==0 and n/1:
#     print("true")
# elif n/n and n%2==0:
#     print ("fails")
#______________________7________________________

# n = int(input("Enter number ---->: "))

# max_sum = 0
# x = 0

# i = 0
# while i < n:
#     num = int(input("Enter number ------>: "))
    
    
#     y = 0
#     temp = num
#     while temp > 0:
#         y += temp % 10
#         temp //= 10
    
  
#     if y > max_sum:
#         max_sum = y
#         x = num
    
#     i += 1
 


# print(f"Num 1: {x}")
# print(f"Num 2: {max_sum}")



#___________________________8___________________
# x= int(input("Enter number =",))


# for i in range(x):
   
#     print(' ' * (x- i - 1), end='')
    
#     print('#' * (2 * i + 1))
#______________________9______________________
# n = int(input("Enter number"))
# number = 1
# for i in range(1, n+1):
    
#     print(' ' * (n - i), end='')
    
  
#     for j in range(i):
#         print(f"{number} ", end='')
#         number += 2
    
    
#     print()
#_______________`________10____________
 
#_____________________6______________

# number = int(input("enter number"))  
# factorial = 1

# while number > 0:
#     factorial *= number
#     number -= 1``

# print(factorial)

#_________________________1______________________

# N = int(input("Enter number"))


# current_number = 1


# while current_number <= N:
    
#     cube = current_number ** 3
   
#     print(f"{current_number}  = {cube}")
  
#     current_number += 1
#_________________________2______________________

# anun = input("Nermucel anuny ")
# gumar = int(input("gumari chapy"))


# print(gumar)


# while True:
#     partq = int(input("inchan eq nermucum hima "))
    
#     if partq>= gumar:
#         print(anun ," shnorhakalutyun dzer partqy marvac e ")
#         break
#     else:
#         print(". pordzeq evs mek angam")

#_________________________3______________________
# number = int(input("Mutqagrel tivy "))

# tiv = 0


# if number == 0:
#     tiv = 1
# else:
 
#     while number != 0:
#         number //= 10 
#         tiv += 1 


# print(f"tveri  qanaky: {tiv}")

#_________________________4______________________
# positive_count = 0
# negative_count = 0


# while True:
#     number = int(input("NErmucel tver "))
    
#     if number == 0:
#         break  
#     if number > 0:
#         positive_count += 1  
#     elif number < 0:
#         negative_count += 1  


# print(f"Drakan tveri qanaky {positive_count}")
# print(f"bacasakan tveri qanaky  {negative_count}")
#_________________________6______________________
# x = int(input("Avandi gumary: "))
# y = int(input("gumary: "))
# z = int(input("Tarekan tokosy: "))


# current_amount = x
# years_passed = 0


# while current_amount < y:
#     current_amount += (current_amount * z) // 100
#     years_passed += 1  


# print(f"{y} kancin {years_passed} tari։")
#_________________________1______________________
# total_salary = 0
# number_of_months = 12


# for month in range(1, number_of_months + 1):
#     monthly_salary = float(input(f"mutqagrel amsekan ashxatavrdzy "))
#     total_salary += monthly_salary


# average_salary = total_salary / number_of_months


# print("Tarekan mijin ashxatavardzy =", average_salary)
#_________________________3______________________
# a = int(input("Մուտքագրեք առաջին թիվը (a): "))
# b = int(input("Մուտքագրեք երկրորդ թիվը (b): "))


# sum_of_numbers = 0
# count = 0


# for number in range(a, b + 1):
#     if number % 3 == 0: 
#         sum_of_numbers += number
#         count += 1


# if count > 0:
#     average = sum_of_numbers / count
#     print(f"Միջին թվաբանականը [a; b] հատվածի թվերի, որոնք բաժանվում են 3-ի, հավասար է {average}-ի")
# else:
#     print(f"[a; b] հատվածում չկա թիվ, որը բաժանվում է 3-ի:")
#______________________5_________________________
# x =int(input("Enter number"))
# for number in range(10, 100):
   
#     tens = number // 10
#     units = number % 10
    
#     if number == 3 * (tens * units):
#         print(number)
#______________________1_________________________

# mylist=["HancagorcMusrapravod",'txa','es','urodliviy', 'bari']
# mylist.sort(key=len,reverse=True )
# print(mylist[0])

# mylist = [7, 4, 4, 4, 5, 6, 6, 9, 1, 0, 1, 2, 2, 3, 2, 4, 6]
# for i in mylist:
#     if i % 2 == 0:
#         mylist.del(i)
# print(mylist)
#-----------------------------------------------------------------------------
# my_list = ["nush", "banan", "dexdz", "xndzor"]

# if my_list:
    
#     x = max(my_list, key=len)
#     print(f"Amena erkar bary '{x}'")
# else:
#     print("The list is empty.")
#------------------------------------------------------------------------------
# list1 = [1, 11, 3, 4, 5]
# list2 = [1,5,6, 7, 8, 9]

# for i in list1:
#     if i in list2:
#         x = True
#         break  
# print(x)

#---------------------------------2-----------------------------------------------
# my_list = ["Hp", "Asus", "Dell", "Mac", "Lenovo"]
# x = "Mac" in my_list
# print(x)
#---------------------------------6-----------------------------------------------
# x = "nermucvac apranqi arjeqy 50 $ e"


# list = x.split()

# print(list)
#---------------------------------5-----------------------------------------------

# word = "RACECAR"


# word_lower = word.lower()


# if word_lower == word_lower[::-1]:
#     print("Open")
# else:
#     print("Trash")

#---------------------------------7-----------------------------------------------

# input_string = "12 21 15 19 8"

# numbers = input_string.split()


# even_numbers = [num for num in numbers if int(num) % 2 == 0]

# print(" ".join(even_numbers))

#0-------------------------------------------------------------------------------

# import random


# suits = ['♠', '♣', '♥', '♦']  
# ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']  


# deck = [rank + suit for suit in suits for rank in ranks]
# n = len(deck)
# for i in range(n - 1, 0, -1):
#     j = random.randint(0, i)
   
#     deck[i], deck[j] = deck[j], deck[i]


# num_players = 4


# hands = {f"Player {i+1}": deck[i*8:(i+1)*8] for i in range(num_players)}


# for player, cards in hands.items():
#     print(f"{player}: {', '.join(cards)}")

#_________________________________________1_________________________________________
    
# vowel_list = [char for char in input("Enter text ") if char.lower() in "abcdefgjklmnopqrestuvw"]

# print("Nermucvac texty:", vowel_list)
# print("Erkarutyuny:", len(vowel_list))
#_________________________________________2_________________________________________
# numbers = []

# # Read input from the user until a blank line is entered
# while True:
#     user_input = input("Enter a number (or press Enter to finish): ")
#     if user_input == '':
#         break  # Exit the loop if a blank line is entered
#     numbers.append(float(user_input))  # Convert input to float and add it to the list

# # Check if any numbers were entered
# if numbers:
   
#     average = sum(numbers) / len(numbers)
#     print(f"\nAverage: {average:.2f}")

  
#     print("Below average values:", [num for num in numbers if num < average])
#     print("Average values:", [num for num in numbers if num == average])
#     print("Above average values:", [num for num in numbers if num > average])
# else:
#     print("No numbers were entered.")

#_________________________________________118_________________________________________
# import string


# sentence = input("Enter a sentence: ")


# cleaned_sentence = ''.join(char.lower() for char in sentence if char not in string.punctuation)


# words = cleaned_sentence.split()


# if words == words[::-1]:
#     print("The entered sentence is a word by word palindrome.")
# else:
#     print("The entered sentence is not a word by word palindrome.")

#_________________________________________117_________________________________________

# import string

# sentence = input("Enter a string: ")


# punctuation = ",.?-!'\":;"

# words = []


# for word in sentence.split():
    
#     cleaned_word = word.strip(punctuation)
#     #
#     if cleaned_word:
#         words.append(cleaned_word)


# print("Words with punctuation removed:", words)

#_________________________________________116_________________________________________
# perfect_numbers = []


# for n in range(1, 10001):
   
#     sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    
  
#     if sum_of_divisors == n:
#         perfect_numbers.append(n)


# print("Perfect numbers between 1 and 10,000:", perfect_numbers)
#_________________________________________115_________________________________________
# x = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# result = []
# m, n = len(x), len(x[0]) 
# i, j = 0, 0
# while len(result) < m * n:
#     while j < n and x[i][j] != None:
#         result.append(x[i][j])
#         x[i][j] = None
#         j += 1
#     j -= 1
#     i += 1
#     while i < m and x[i][j] != None:
#         result.append(x[i][j])
#         x[i][j] = None
#         i += 1
#     i -= 1
#     j -= 1
#     while j >= 0 and x[i][j] != None:
#         result.append(x[i][j])
#         x[i][j] = None
#         j -= 1
#     j += 1
#     i -= 1
#     while i >= 0 and x[i][j] != None:
#         result.append(x[i][j])
#         x[i][j] = None
#         i -= 1
#     i += 1
#     j += 1
# print(result)
# -----------------------N138------------------------  

# dictionary = {
#        1:"./?/",
#        2:"ABC",
#        3:"DEF",
#        4:"GHI",
#        5:"JKL",
#        6:"MNO",
#        7:"PQRS",
#        8:"TVU",
#        9:'WXYZ'
#        0:"",
       
       
       
#        }
# message = input('Enter messege:  ').upper()
# result = ''
# for char in message:
#     if 
#         result += dictionary[i]
# print(result)

# ------------------------N139------------------------  

# dictionary = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
#     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.' } 
# message = input('Enter messege:  ').upper()
# result = ''
# for i in message:
#     if i in dictionary:
#         result += dictionary[i]
# print(result)

# ------------------------N140------------------------  

# states_and_territories = {
#     'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island',
#     'E': 'New Brunswick', 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
#     'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
#     'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta', 'V': 'British Columbia',
#     'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'
# }
# postal_code = input('Enter posal code:  ').strip(' ').upper().replace(' ', '')
# if postal_code[0] not in states_and_territories:
#     print('ERROR')
# else:
#     if postal_code[1].isdigit():
#         if postal_code[1] == '0':
#             address_type = 'rural'
#         else:
#             address_type = 'urban'
# print(f'{states_and_territories[postal_code[0]]}, {address_type}')

# ------------------------N142?------------------------  
# singural_letters = []
# text = input('Enter text:  ')
# count = 0
# for i in text:
#     if i not in singural_letters:
#       singural_letters += i
# print(singural_letters)
# for i in singural_letters:
#    count += 1
# print(f'Count Singular Letters - {count}')

# ------------------------N143--------------------------

# word1 = input('Enter text:  ')
# word2 = input('Enter text:  ')
# word_1 = ('')
# word_2 = ('')
# for i in word1:
#    if i.isalpha():
#       word_1 += i
# for i in word2:
#    if i.isalpha():
#       word_2 += i
# print(sorted(word_1) == sorted(word_2))

# units = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine'
# }

# ten_to_twenty = {
#     10: 'ten',
#     11: 'eleven',
#     12: 'twelwe',
#     13: 'thrteen',
#     14: 'fourteen',
#     15: 'fivteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'ninteen'
# }

# tens = {
#     20: 'twenty',
#     30: 'thrty',
#     40: 'fourty',
#     50: 'fivty',
#     60: 'sixty',
#     70: 'seventy',
#     80: 'eihty',
#     90: 'ninty'
# }


# number=int(input("Enter number"))
# print(units[number])


# --------------------------------------------------------------------------------------------------------------------
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Cannot divide by zero."
#     return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     while True:
#         choice = input("Enter choice (1/2/3/4): ")

#         if choice in ('1', '2', '3', '4'):
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
#             except ValueError:
#                 print("Invalid input. Please enter numbers only.")
#                 continue

#             if choice == '1':
#                 print(f"{num1} + {num2} = {add(num1, num2)}")

#             elif choice == '2':
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")

#             elif choice == '3':
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")

#             elif choice == '4':
#                 result = divide(num1, num2)
#                 print(f"{num1} / {num2} = {result}")

#         else:
#             print("Invalid input. Please select a valid option.")

#         next_calculation = input("Do you want to perform another calculation? (yes/no): ")
#         if next_calculation.lower() != 'yes':
#             break

# calculator()
# def pifagor(a:int|float,b:int|float) ->int|float:
#     c=(a**2+b**2)
# def has_duplicate_grade(grades, grade):
#     return grades.count(grade) > 0

# def main():
#     group_size = 3
#     total_groups = 2
#     total_students = group_size * total_groups

#     groups = [[] for _ in range(total_groups)]
#     grades = []

#     print(f"Մուտքագրեք {total_students} ուսանողների անունները և նրանց գնահատականները:")

#     for g in range(total_groups):
#         print(f"Խումբ {g + 1}:")
#         for i in range(group_size):
#             name = input(f"Ուսանող {i + 1} -ներմուծեք անունը: ")
            
#             while True:
#                 try:
#                     grade = int(input(f"Ուսանող {i + 1} - Ներմուծել գնահատականը (0-100): "))
#                     if grade < 0 or grade > 100:
#                         print("Գրեք ճիշտ գնահատական (0-100):")
#                         continue
#                     if has_duplicate_grade(grades, grade):
#                         print("Այս գնահատականը արդեն գոյություն ունի: Նվիրեք նոր գնահատական:")
#                         continue
#                     break
#                 except ValueError:
#                     print("Խնդրում ենք ներմուծել թիվ (0-100):")

#             grades.append(grade)
#             groups[g].append({'name': name, 'grade': grade})

#     for g in range(total_groups):
#         print(f"\nԽումբ {g + 1}:")
#         for student in groups[g]:
#             print(f"Ուսանող: {student['name']}, Գնահատական: {student['grade']}")

# if __name__ == "__main__":
#     main()

# -----------------------N138------------------------  

# dictionary = {
#         '1': '1', '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
#         'A': '2', 'B': '22', 'C': '222', 'D': '3', 'E': '33', 'F': '333',
#         'G': '4', 'H': '44', 'I': '444', 'J': '5', 'K': '55', 'L': '555',
#         'M': '6', 'N': '66', 'O': '666', 'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#         'T': '8', 'U': '88', 'V': '888', 'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#         ' ': '0'}
# message = input('Enter messege:  ').upper()
# result = ''
# for i in message:
#     if i in dictionary:
#         result += dictionary[i]
# print(result)

# ------------------------N139------------------------  

# dictionary = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
#     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.' } 
# message = input('Enter messege:  ').upper()
# result = ''
# for i in message:
#     if i in dictionary:
#         result += dictionary[i]
# print(result)

# ------------------------N140------------------------  

# states_and_territories = {
#     'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island',
#     'E': 'New Brunswick', 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
#     'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
#     'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta', 'V': 'British Columbia',
#     'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'
# }
# postal_code = input('Enter posal code:  ').strip(' ').upper().replace(' ', '')
# if postal_code[0] not in states_and_territories:
#     print('ERROR')
# else:
#     if postal_code[1].isdigit():
#         if postal_code[1] == '0':
#             address_type = 'rural'
#         else:
#             address_type = 'urban'
# print(f'{states_and_territories[postal_code[0]]}, {address_type}')

# ------------------------N142------------------------  
# singural_letters = []
# text = input('Enter text:  ')
# count = 0
# for i in text:
#     if i not in singural_letters:
#       singural_letters += i
# print(singural_letters)
# for i in singural_letters:
#    count += 1
# print(f'Count Singular Letters - {count}')


# ------------------------N143--------------------------

# word_1 = input('Enter word:  ').lower() 
# word_2 = input('Enter word:  ').lower()
# result1 = {}
# result2 = {}
# for i in word_1:
#     if i in result1:
#         result1[i] += 1  
#     else:
#         result1[i] = 1
# for i in word_2:
#     if i in result2:
#         result2[i] += 1
#     else:
#         result2[i] = 1
# print(result1 == result2)

# ------------------------N144--------------------------

# sentence_1 = input('Enter sentence:  ').lower() 
# sentence_2 = input('Enter sentence:  ').lower()
# sentence_1 = sentence_1.replace(' ', '')
# sentence_2 = sentence_2.replace(' ', '')
# result1 = {}
# result2 = {}
# for i in sentence_1:
#     if i in result1:
#         result1[i] += 1  
#     else:
#         result1[i] = 1
# for i in sentence_2:
#     if i in result2:
#         result2[i] += 1
#     else:
#         result2[i] = 1
# print(result1 == result2)

# ------------------------N145--------------------------
# word = input('Enter word:  ').upper()
# mydict = {
#     'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }
# result = 0
# for i in word:
#     if i in mydict:
#         result += mydict[i]
# print(result)
#______________________________________________________________
# import random

# def generate_password():
 
#     length = random.randint(7, 10)
    
#     password = ''.join(chr(random.randint(33, 126)))
#     for a in range(length)
#     return password

# if __name__ == "__main__":
 
#     random_password = generate_password()
#     print(f"Generated Password: {random_password}")
# import string
# import random
# alphabe=string.ascii_upperacse
# digits=string.digits
# def  generate_car_number ()->str:
#     car_number=random.choices(digits,k=4)+random.choice(alphabe,k=3)
#     return  car_number
# car_number=generate_car_number
#---------------------------------------------------------------------------------------------------------------------------------------
# mydict = {
#     'a':1,
#     'b':5,
#     'c':7
# }
# print(mydict['Ճ'])
# print(mydict.get('a', 'BRO JAN CHKA'))
# del mydict['a']
# print(mydict)
# mydict.pop('a')
# print(mydict)
# mydict['a'] = 77
# mydict['Ճ'] = 10
# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
# list1 = ['BMW3', 'BMW5', 'BMW7', 'Cruze']
# list2 = ['Albert', 'Arman', 'Vahag', 'Avo']
# dict_ = {}
# for i, j in zip(list1, list2):
#     dict_[i] = j
# print(dict_)
# print({i:j for i, j in zip(list1, list2)})
# mydict = {
#     'Yura':-6,
#     'Sergey':3,
#     'Sergo':2,
#     'Tigran':7
# }
# my_values = sorted(mydict.values())
# # my_keys = sorted(mydict.keys())
# my_keys = sorted(mydict, key=mydict.get)
# mydict = {i:j for i, j in zip(my_keys, my_values)}
# print(mydict)
# mylist = ['a', 'b', 'c', 'e', 'a']
# for i in range(0, len(mylist)):
#     print(i, mylist[i])
# for i in enumerate(mylist):
#     print(i)
# student = {
#   "name": "Emma",
#   "class": 9,
#   "marks": 75
# }
# del student
# # student.clear()
# print(student)
# x = {
#     'bararan':[1, 2, 3],
#     1:3
# }
# print(x)
# sampleDict = dict([
#     ('first', 1),
#     ('second', 2),
#     ('third', 3)
# ])
# print(sampleDict.items())

# {'a':6, 'b':6, 'c':11}



# def matryoshka(lst):
    
#     sorted_lst = sorted(lst, key=lambda x: (min(x), -max(x)))
    

#     for i in range(1, len(sorted_lst)):
#         min_prev = min(sorted_lst[i - 1])
#         max_prev = max(sorted_lst[i - 1])
#         min_curr = min(sorted_lst[i])
#         max_curr = max(sorted_lst[i])
        
#         if not (min_curr > min_prev and max_curr < max_prev):
#             return False
    
#     return True


# print(matryoshka([[2, 3, 9, 5], [10, 2, 1]]))   


# print(matryoshka([[4, 5], [6, 3]]))  


# print(matryoshka([[7, 1], [7, 6, 5, 4, 3, 2]])) 

# print(matryoshka([[1, 5], [2, 6]])) 


# print(matryoshka([[1, 2, 3, 4], [0, 3, 5], [2, 2, 3]]))  
 
#________________________________________________________________________
# def describeList(lst):
#     if len(lst) == 0:
#         return "empty"
#     elif len(lst) == 1:
#         return "singleton"
#     else:
#         return "longer"
#__________________________________________________
# def update_light(current):
#     if current == "green":
#         return "yellow"
#     elif current == "yellow":
#         return "red"
#     elif current == "red":
#         return "green"
#     else:
#         raise ValueError("Invalid traffic light state")
    #-----------------------------------------------------
#     def tribonacci(signature, n):
    
#     if n <= len(signature):
#         return signature[:n]
    
    
#     result = signature[:]
#     while len(result) < n:
#         next_value = result[-1] + result[-2] + result[-3]
#         result.append(next_value)
    
#     return result
# print(tribonacci([1, 1, 1], 10))  
# print(tribonacci([0, 0, 1], 10))  
# print(tribonacci([3, 2, 1], 5))   
# print(tribonacci([0, 0, 0], 5)) 
#___________________________________________________________
#    
#  mylist = [4, 8, 14, 30, 52, 136, 189, 365, 785, 1235, 2030, 3045]
# n = 2030
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if mylist[mid] == n:
#         print(mid)
#         break
#     elif mylist[mid] < n:
#         start = mid + 1
#     else:
#         stop = mid - 1


###########################################################################################



######################################################################################33

# class Solution(object):
#     def maxArea(self, height):
    
#         left = 0
#         right = len(height) - 1
#         max_area = 0

#         while left < right:
            
#             width = right - left
#             current_height = min(height[left], height[right])
#             current_area = width * current_height
            
            
#             max_area = max(max_area, current_area)

            
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_area

# #
# solution = Solution()
# height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height2 = [1, 1]
# print(solution.maxArea(height1))  
# print(solution.maxArea(height2))





# def head(filename):
#     try:
#      with open(filename,'r') as file:
#             x =file.read()
#             x =x.sort(key=len)
#             print(x[-1])
#      except FileExistsError:
# print ("Erroe")




#--------------------------------------------
# import time

# class Book:
#     def __init__(self, title="Unknown", author="Unknown", year=0):
#         self.title = title
#         self.author = author
#         self.year = year
#         print("Book created by constructor.")

#     def __del__(self):
#         print(f"Book object destroyed: {self.title} by {self.author}")

#     def calculate_book_age(self):
#         current_year = time.localtime().tm_year
#         return current_year - self.year

#     def calculate_days_since_publication(self):
#         days_in_year = 365
#         current_year = time.localtime().tm_year

    
#         if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
#             days_in_year = 366

#         return self.calculate_book_age() * days_in_year

#     def get_book_info(self):
#         return (f"Title: {self.title}\n"
#                 f"Author: {self.author}\n"
#                 f"Year: {self.year}\n"
#                 f"Book Age: {self.calculate_book_age()} years\n"
#                 f"Days Since Publication: {self.calculate_days_since_publication()} days\n")


# if __name__ == "__main__":
#     book1 = Book("War and Peace", "Leo Tolstoy", 1869)
#     print(book1.get_book_info())

#     title = input("Enter book title: ")
#     author = input("Enter book author: ")
#     year = int(input("Enter book year: "))

#     book2 = Book(title, author, year)
#     print(book2.get_book_info())


##----------------------------------------
# def word(filename):
#     try:
#         with open(filename,"r") as file:
            
#             print("x")
#     except FileNotFoundError:
#       print("chka")
# word("1.txt") 
  




#--------------------------------150----------------------
# import sys

# def tail(filename, n=10):
#     try:
#         with open(filename, 'r') as file:
#             lines = []
#             for line in file:
#                 lines.append(line)
#                 if len(lines) > n:
#                     lines.pop(0)
#             for line in lines:
#                 print(line, end='')
#     except FileNotFoundError:
#         print(f"file'{filename}' chka.")
#     except Exception as e:
#         print(f"chkaaaa: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("nmanatip ban chka.")
#     else:
#         tail(sys.argv[1])

#--------------------------------151----------------------
# import sys

# def cat(filenames):
#     if not filenames:
#         print("Չեն նշվել ֆայլեր կարդալու համար։")
#         return

#     for filename in filenames:
#         try:
#             with open(filename, 'r') as file:
#                 print(file.read(), end='')
#         except:
#             print(f"filey chajoxvec '{filename}' bacel։")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("file chka։")
#     else:
#         cat(sys.argv[1:])
#--------------------------------152----------------------



# source_file = input("Mutqagrel arajin anuny: ")
# target_file = input("mutqagrel nor anuny: ")

# #
# with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
#     for idx, line in enumerate(src, 1):
        
#         tgt.write(f"{idx}: {line}")
        
# print("hamarakalvel ev pahvel en nor fileum  :")


#--------------------------------153----------------------

# filename = input("Filei anuny: ")


# with open(filename, 'r') as file:
#     words = file.read().split()  


# max_length = max(len(word) for word in words)


# longest_words = [word for word in words if len(word) == max_length]


# print(f"bari erk: {max_length}")
# print("barer nuny erk:")
# for word in longest_words:
#     print(word)
#--------------------------------155----------------------
# import string


# filename = input("grel file i anunay: ")


# with open(filename, 'r') as file:
#     word_count = {}
    
   
#     for line in file:
        
#         line = line.translate(str.maketrans('', '', string.punctuation)).lower()
#         words = line.split()

       
#         for word in words:
#             word_count[word] = word_count.get(word, 0) + 1


# max_count = max(word_count.values())
# most_common_words = [word for word, count in word_count.items() if count == max_count]


# print(f"Amenahachax handipox barery {max_count} angam:")
# print("amenashaty:")
# for word in most_common_words:
#     print(word)

#--------------------------------156----------------------


# total_sum = 0  

# while True:
#     user_input = input("Mutqagrel tivy: ")

#     if user_input == "":  
#         break

#     try:
#         number = float(user_input)  
#         total_sum += number  
#         print(f"yndanur {total_sum}")
#     except ValueError:  
#         print("mutqagri tiv ։")

# print(f"verjnakan : {total_sum}")
#--------------------------------173----------------------
# total_sum = 0.0  

# while True:
#     user_input = input("nermucel  tivy ")

#     if user_input == "":  
#         break

#     try:
#         number = float(user_input)  
#         total_sum += number  
#     except ValueError: 
#         print("nermucel tivy kam sexmir enter ")

# print(f"arjeq: {total_sum}")
#----------------------------------------------------
with open
