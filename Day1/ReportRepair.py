file = open('input.txt').readlines()
input_data = []
for s in file:
    s.rstrip('\n ')
    input_data.append(s)
found = False
for i in input_data:
    for j in input_data:
        sum = int(i) + int(j)
        if(sum == 2020):
            found = True
            first = i
            second = j
            multiplied = int(i) * int(j)
            break
print(first, "and", second)
print(multiplied)
