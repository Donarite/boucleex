
'''
secret_number = 777
print( """           +================================+
           |Welcome to my game, muggle!     |
           | Enter an integer number        |
           | and guess what number I've     | 
           | picked for you.                |
           | So, what is the secret number? |
           +================================+ """)
Nombre_choisi = int(input("Entre un nombre entier "))
while Nombre_choisi != secret_number:
    print("Ce n'est pas le bon numéro trou du cul ")
    Nombre_choisi = int(input("Entre un nombre entier "))
print("Bien ouej mon gars tu peux partir")
'''


'''
import time
for i in range(5,0, -1):
    print(i)
    time.sleep(1)
print("PLANQUEZ VOUS OU JVOUS bip ")
'''
'''
user_word = input("Entre un mot et plus vite que ça: ")
user_word = user_word.upper()
voyelles = "AEIOU"
word_without_voy = ""

for letter in user_word:
    if letter not in voyelles:
        word_without_voy += letter
        print(letter)
print(word_without_voy)
'''

'''
Nbr_Bloc = int(input("Entrez le nombre de bloc "))
Etage = 0
n = 1
while Nbr_Bloc >= n:
    Nbr_Bloc -= n
    n += 1
    Etage += 1


print("Le nombre d'étage est:" , Etage)
'''
'''
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)
numbers[0] = 111
print("\nPrevious list content:", numbers)
numbers[1] = numbers[4]
print("Previous list content:", numbers)
print("\nList length:", len(numbers))

print(numbers[-5])
'''
'''
Chapeau = [1,2,3,4,5]
numbers = input("Entrer un nombre entier ")
Chapeau[3] = int(numbers)
del Chapeau[4]
print(Chapeau)
print(len(Chapeau))
'''
'''
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append(4)
print(len(numbers))
print(numbers)
numbers.insert(0, 222)
print(len(numbers))
print(numbers)
numbers.insert(0,333)
print(numbers)
'''
'''
groupe = []
groupe.append("Johan le preteur")
groupe.append("Denis")
groupe.append("yoan")
print(groupe)
for i in range(0,2):
    new = input("ajouter de nouveaux membres ")
    groupe.append(new)
print(groupe)
del groupe[4]
groupe.insert(0,'Erwin')
print(groupe)
'''
'''
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))
for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("\nSorted:")
print(my_list)
'''
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)




















