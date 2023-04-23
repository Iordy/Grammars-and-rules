def check_word(grammar, start_symbol, word):
    if len(word) == 0 and 'l' in grammar[start_symbol]:
        print("acceptat")
        return True
    
    for tup in grammar[start_symbol]:
        if word and word[0] == tup[0] and tup[0].islower():
            if check_word(grammar, tup[1], word[1:]):
                return True
            
        elif tup[0].isupper():
            check_word(grammar, tup[0], tup[1]+word)
                
    
    return False

grammar = {'S':[('a', 'A'), ('d', 'E')],'A':[('a', 'B'), ('a', 'S')], 'B':[('b', 'C')], 'C':[('b', 'D'), ('b', 'B')], 'D':[('c', 'D'),'l'], 'E':['l']}
start_symbol = 'S'
string = "aabbcc"
#
#print(check_word(grammar, start_symbol, string))







