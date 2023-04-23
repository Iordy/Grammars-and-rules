import grammar




class Grammar:
    def __init__(self, start_symbol, grammar, alphabet, non_terminals):
        self.start_symbol = start_symbol
        self.grammar = grammar
        self.alphabet = list(set(alphabet))
        self.non_terminals = list(set(non_terminals))
                        
    
    
    def check_word(self, start_symbol, word):
        if len(word) == 0 and 'l' in self.grammar[start_symbol]:
            return True
        
        for tup in self.grammar[start_symbol]:
            if word and word[0] == tup[0] and tup[0].islower():
                if self.check_word(tup[1], word[1:]):
                    return True
                
            elif tup[0].isupper():
                self.check_word(tup[0], tup[1]+word)
                    
        return False




def backtrack(word, lungime):
    if len(word) >= lungime:
        if testing_grammar.check_word('S', word):
            print(word)
               
    else:
            backtrack(word + "a", lungime)
            backtrack(word + "b", lungime)
            backtrack(word + "c", lungime)
            backtrack(word + "d", lungime)
    return



n = int(input("Ce lungime au cuvintele generate?"))
            
            
#print(generate_words("abcd"))


testing_grammar = Grammar('S',{'S':[('a', 'A'), ('d', 'E')],'A':[('a', 'B'), ('a', 'S')], 'B':[('b', 'C')], 'C':[('b', 'D'), ('b', 'B')], 'D':[('c', 'D'),'l'], 'E':['l']} , "abcd", "SABCDE")

#testing_grammar.check_word('S', "aabcc")

print(backtrack("", n))