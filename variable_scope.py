import builtins

print(dir(builtins))

# Local, intermidiate, Global and builtins
 
 x = 'global x'
 
 def outer():
    # global x
    x = 'intermidiate x'
     
    def inner():
        # nonlocal x
        # global x
        x = 'local x'
