class A:
    def __hash__(self):
        return 1
    
    def __eq__(self, other):
        return False
    

x = A()
y = A()

print(hash(x), hash(y))
print(x == y)