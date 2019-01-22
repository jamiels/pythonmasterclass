class RentalUnit:
 def __init__ (self,a,b,c,d,e):
   self.__address = a
   self.__rent = b
   self.__tenant_first = c
   self.__tenant_last = d
   self.__eviction = e
 def get_address(self):
     return self.__address
 def set_rent(self,r):
     if r < 50000:
        self.__rent = r
 def __str__(self):
     print('hey!!')
     return 'hey12345'
 def get_name(self):
   full_name = self.tenant_first + " " + self.tenant_last
   return full_name
 def get_annual_rent(self):
     return 12 * self.__rent
unit1 = RentalUnit("155 East 55th Street", 5000, "John", "Smith", False)
print(unit1.get_annual_rent())
unit1.set_rent(100000000) # unit1.rent = 10000
print(unit1.get_annual_rent())
print(unit1.get_address())
print(unit1.__dir__)
print(unit1.__dict__)
print(unit1.__doc__)
for e in dir(unit1):
    print(e)




'''
print(unit1.get_name())
print(unit1.get_annual_rent())
print(unit1.address)

print(unit1)
'''
