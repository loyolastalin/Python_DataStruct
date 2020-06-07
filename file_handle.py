fhandle = open('one.txt')

file = fhandle.read()
print(file)
print(len(file))
print(file[0:10])
'''
print(fhandle)
for lines in fhandle:
    lines = lines.rstrip()
    print(lines)
'''