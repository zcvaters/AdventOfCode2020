import fileinput

character = []
password = []
args = []
for i in fileinput.input():
    args.append(i.split(' '))
print(args)
bounds = args[0].split('-')


print(bounds[2])
#print(character)
#print(password)

for i in range(len(character)):
    value = bounds[i]
    
    #print(lower)
    #print(upper)

#for i in bounds:
    #bound = i.split('-')
    
