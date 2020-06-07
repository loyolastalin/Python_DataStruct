# default parameter function

def greet_user(name='stalin'):
    print("name : {}".format(name))
    
greet_user()
greet_user('Jhon')

# keyword argument 

def display_name(fistname, lastName):
    print("name : {} {}".format(fistname, lastName))
    
display_name(lastName='soosai', fistname='stalin')
# param array
def disply_parameters(*arg):
    for item in arg:
        print("item type {} and name".format(type(item), item))

disply_parameters('sd', 1, 3)