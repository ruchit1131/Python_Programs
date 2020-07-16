from sys import argv
script,name=argv
prompt='>> '
print(f"so {name} this is {script} script")
print("do you like me")
like=input(prompt)
print(f'''So in this script {script},
 you said your name is {name}
 and for you liking me.. its {like}''') 