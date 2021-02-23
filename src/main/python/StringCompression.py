'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def StringCompression(s:str)->str:
    def compress(s:str)->str:
        if len(s)==0:return ""

        prev = None
        count = 0
        new = ""
        for c in s:
            if c==prev:
                count+=1
            else:
                if prev!=None:
                    new += prev + str(count)
                prev = c
                count = 1
        
        new += prev + str(count)
        return new

    compressed = compress(s)
    print(compressed)
    if len(s)<=len(compressed): return s
    print('compressed')
    return compressed

if __name__=='__main__':
    assert StringCompression('abcc')=="abcc"
    assert StringCompression('aabcccccaaaaaa')=="a2blc5a6"
    assert StringCompression('aabcccccaaa')=='a2blc5a3'
    