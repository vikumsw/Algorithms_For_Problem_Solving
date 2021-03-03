'''
“Reverse the order of words in a given string.”
'''
def ReverseSentence(sen:str)->str:
    l = sen.split()
    rev_sen = ""
    while len(l)>0:
        rev_sen += l.pop()
        if len(l)>0: rev_sen += " "

    return rev_sen 

if __name__ == "__main__":
    assert ReverseSentence("a b c")=="c b a"
