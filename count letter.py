def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz" 
    most_occuring_letter = 0
    frequency = 0  
    letters = []
    for word in word_list:
        for letter in word:
            if letter in ALPHABET:
                letters.append(letter)
    for i in letters:
        if letters.count(i) > frequency:
            frequency = letters.count(i)
            most_occuring_letter = i
            
                
    return most_occuring_letter, frequency

monty_quote =str(input("ENter sentence"))
monty_words = monty_quote.split(" ")
print(count_letters(monty_words))
