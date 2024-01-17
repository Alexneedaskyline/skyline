
b = ["A","E","I","O","U", "a", "i", "e", "o", "u"]
vowel_count = 0
consonant_count = 0

while True:
    a = input("Enter an alphabet : ")
    if a == "quit":
        print("Vowels: ", vowel_count)
        print("Consonants: ", consonant_count)
        break 
    
    elif a in b:
        print(" It's a vowel")
        #(Help)Add one to vowel's counter
        vowel_count += 1
    else:
        print("It's a consonant")
        #(Help)Add one to consonant's counter
        consonant_count += 1
    