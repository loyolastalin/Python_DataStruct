class Multiple:
    value = 100 # class level variable

    def instance_method(self):
        print('instance method')
    
    @classmethod
    def class_method(cls):
        print('class_method ', cls.value)
    @staticmethod
    def static_method():
        print('static_method')
    
a = Multiple()
a.instance_method()
a.class_method()
Multiple.static_method()