#create a dictionary class
class ClassDict:
    def return_dict(self):
        d = {k:k**2 for k in range(1,16)}
        return d
        #print(d)
    
ob = ClassDict()
print(ob.return_dict())