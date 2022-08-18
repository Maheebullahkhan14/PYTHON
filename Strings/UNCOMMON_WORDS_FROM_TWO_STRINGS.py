#uncommon Words from Two Strings 

def uncommon_word(A,B):
    count = {}
    for word in A.split() :
        count[word] = count.get(word , 0)+1

    for word in B.split():
        count[word] = count.get(word,0) + 1
        
    return [word for word in count if count[word] == 1]

        
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
  
# # Print required answer
print(uncommon_word(A, B))

    
    