#list comprehension
# flower=['lilly','lotus','rose','sunflower']
# newflower=['lotus','rose']#contain flowers have letter 'o'
# flowers=['lilly','lotus','rose','sunflower']
# newflowers=[]
# for i in flowers:
#     if 'o' in i:
#         newflowers.append(i)
# print(newflowers)
# list comprehension
# num=[2,3,4,5]
# newnum=[i*i for i in num] #squre of the list
# print(newnum)
# newnum=[i for i in range(1,6)]
# print(newnum)
# newnum=[i*i for i in range(1,6)]
# print(newnum)
# num=[2,3,4,5,6,7,8,]
# newnum=[i for i in num if i%2==0] #print even numbers
# print(newnum)
# num=[2,3,4,5,6,7,8,]
# newnum=[i for i in num if i%2!=0] #print odd numbers
# print(newnum)

# flower=['lilly','lotus','rose','sunflower']
# newflower=[i for i in flower if 'o' in i]
# print(newflower)

# flower=['lilly','lotus','rose','sunflower']
# newflower=[i.upper() for i in flower]
# print(newflower)
# flower=['lilly','lotus','rose','sunflower']
# newflower=['hebiscus' if i!='lilly' else 'lilly' for i in flower ]
# print(newflower)

# flower=['lilly','lotus','rose','sunflower']
# newflower=[i if i!='sunflower' else 'hebiscus' for i in flower ]
# print(newflower)
# flower=['lilly','lotus','rose','sunflower']
# newflower=[i.replace('sunflower','hebiscus') for i in flower]
# print(newflower)
# #
# num=[1,2,3,4,5,6]
# newnum=['even' if i%2==0 else 'odd' for i in num]
# print(newnum)

list=[1,2,3,4,5,6,7,8,9]
newnum=[i*i if i%2!=0 else i for i in list]
print(newnum)



