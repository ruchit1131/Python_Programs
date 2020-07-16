import random
from urllib.request import urlopen
import sys

WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

PHRASES={
    "class%%%(%%%):":"Make a class named %%% that is -a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":"class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":"class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":"From *** get the *** attribute and set it to '***'."
        }#just another dictionary

#do they want to drill phrases first
if len(sys.argv)==2 and sys.argv[1]=="english":
    PHRASE_FIRST=True
else: PHRASE_FIRST=False

#load up the words form the website

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))#original word loaded from website is: b'cave\n' we get the word in this way. When we strip it i.e  b'cave\n'.strip()
    #it becomes  b'cave' which is utf-8 format. now we need to convert it into string by decoding it, So we use str(word.strip, encoding="utf-8".
    #word.strip()will remove the first and last spaces form the word.If the word was
    #"fsssss".strip("f") then it will remove all f's on either ends. Result will be "sssss". For "fsssss".strip("s") result="f"(all s at the end removed)
    #for "fsssss".strip("fs") all f and s on the ends are removed. the answer is "" an empty string

def convert(snippet,phrase):
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]#w.capitalise() will convert the strings
    #into the format that first letter will be capitalized and other small. "".count("%%%") function will count the no of occurances of "%%%"(SUBSTRING) in the string 

    other_names=random.sample(WORDS,snippet.count("***"))
    results=[]
    param_names=[]

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)#random.randint(1,3) will return no. from 1,2or 3 in a random manner
        param_names.append(', '.join(random.sample(WORDS, param_count)))#"str".join(l) where l is a list or tuple of a dictionary(only the key values will be joined)
                                                                        #will make a bigger string comprising of all smaller strings with "str" as delimiter and all
                                                                        #the values in the list/tuple/dict are strings.
    for sentence in snippet, phrase:
        result = sentence[:] # it will copy the whole list sentence in result form index 0 to where ever it ends. we can also write result=sentence[0:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)#replace the 1st occuring "%%%" with word 

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
    
        results.append(result)

    return results

try:#exception handling
    while True:
        snippets = list(PHRASES.keys())#list of the keys of the dictionary PHRASES
        random.shuffle(snippets)#it will shuffle the list 'snippets' in an random order

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)#pass the respective snippet and phrase i.e key and value in convert function
            if PHRASE_FIRST:
                question, answer = answer, question#swapping values

            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")

