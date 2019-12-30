mydictionary={(1,1):'Erik',(1,2):'Sara',(2,3):'Vera',(2,1):'Samuel'}

with open('mydictionary.txt', 'w') as f:
    print(mydictionary, file=f)


with open('mydictionary.txt', 'r') as f: 
    content = f.read()
    dic = eval(content);

print(dic)

print(dic.values())
print(max(dic))
