print("Pig Latin Translator\n\n")


def translate():
    user_string = input("Please enter a sentence to translate in Pig Latin:")
    split_string = []
    split_string = user_string.split()


    string_join = " ".join(split_string)


    vowels = ["a","e","i","o","u","y"]
    cap_vowels = ["A","E","I","O","U","Y"]
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cap_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_char = ["!",",",".","@","#","$","%","^","&","*","(",")","?","<",">"]

    for word in range(len(split_string)):
        translated_word = []
        word_char = list(split_string[word])
        
       
        for eachchar in range(len(word_char)):
            allvowels=0
            if (word_char[eachchar] in vowels) or (word_char[eachchar] in cap_vowels):
                allvowels+=1
        if allvowels==(len(word_char)):
            translated_word.append("".join(word_char))
            translated_word.append("yay")
            combined_translated_word = "".join(translated_word)
            split_again = list(combined_translated_word)
                    
            for eachletter in range(len(split_again)):
                if (split_again[eachletter] not in alphabets) and  (split_again[eachletter] not in cap_alphabets):
                    split_again.append(split_again[eachletter])
                    split_again[eachletter] = ""
            combined_again = "".join(split_again)        
            split_string[word] = combined_again
        else:        
            for eachchar in range(len(word_char)):
                if (word_char[eachchar] in vowels) or (word_char[eachchar] in cap_vowels):
                        
                    translated_word.append("".join(word_char[eachchar:]))
                    translated_word.append("".join(word_char[0:eachchar]))
                    translated_word.append("ay")
                        
                    combined_translated_word = "".join(translated_word)
                    split_again = list(combined_translated_word)
                        
                    for eachletter in range(len(split_again)):
                        if (split_again[eachletter] not in alphabets) and  (split_again[eachletter] not in cap_alphabets):
                            split_again.append(split_again[eachletter])
                            split_again[eachletter] = ""
                    combined_again = "".join(split_again)        
                    split_string[word] = combined_again
                    break


    for word in range(len(split_string)):
        for anychar in split_string[word]:
            if anychar in cap_alphabets:
                wordd = str(split_string[word])
                wordd = wordd.title()
                split_string[word] = wordd
                

    combined_translated_string = " ".join(split_string)
    print("Your translated string is                        :",combined_translated_string)
        





user_bool = input("Do you want to translate? (y/n) :")
user_bool = user_bool.lower()
while user_bool!='n':
    translate()
    user_bool = input("Do you want to translate more? (y/n) :")

