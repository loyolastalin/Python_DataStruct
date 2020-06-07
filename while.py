secrect_number = 9

count =0
while(count < 3):
    guess = int(input('guess : '))
    count+=1
    if guess == secrect_number:
        print('you won!')
        break
else: # excecute if no break
    print('Sorry')
    