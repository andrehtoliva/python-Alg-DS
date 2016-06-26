def reverse_words1(s):
    return " ".join(reversed(s.split()))
    
def rev_word(s):
    
    words = []
    length = len(s)
    space = [' ']
    
    i = 0
    
    while i < length:
        
        if s[i] not in space:
            word_start = i
            
            while i < length and s[i] not in space:
                i += 1
                
            words.append(s[word_start:i])
            
        i += 1
        
    return " ".join(reversed(words))

print reverse_words1("Andre vai ser contratado")
print rev_word("Andre vai ser contratado")
    
    
    