l = input("Enter a sentence: ")
vowel = ['a','e','i','o','u']
string = ''
l = l.split()
a = 0
for i in l:
    k = ''
    string = ''
    for j in range(len(i)):
        if (i[j] not in vowel):
            string = string + i[j]
            if j == len(i) - 1:
                break
            if (i[j+1] not in vowel):
                pass
            else:
                k = k + i[j+1:]
                break
        else:
            k = k + i[j]
            pass
    string = string + 'ay'
    k = k + string
    l[a] = k
    a = a + 1
string = ''
for i in l:
    string = string + i + ' '

print("Pig Latin form: " + string)
    
        
    
