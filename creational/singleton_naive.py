
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls,*args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance

        return cls._instances[cls]

class SingletonClass(metaclass = SingletonMeta):
    def perform_something(self):
        pass


def main():
    s1 = SingletonClass()
    s2 = SingletonClass()
    if id(s1)==id(s2):
        print('Singleton Classes are working perfectly fine')
    else:
        print('Singleton Classes are not working')


if __name__=='__main__':
    main()