def solution():
    #def is used to define a function 
    ## input the phrase
    phrase = input("Enter the phrase: ")
    ## split the phrase into substrings
    phrase_split = phrase.split()
    #so now we first have to declare what acronym is and since it might take a garbage value we give it as an empty string 
    acronym =""
    ## iterate through every substring
    for i in phrase_split:
        acronym = acronym + i[0].upper()

    print("The acronym for your phrase is ",acronym + ".")

solution()
