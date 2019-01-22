class RentalUnit:
 def get_name(self):
   full_name = self.tenant_first + " " + self.tenant_last
   return full_name
 def get_annual_rent(self):
     return 12 * self.rent


unit1 = RentalUnit()
unit1.address = "155 East 55th Street"
unit1.rent = 5000
unit1.tenant_first = "John"
unit1.tenant_last = "Smith"
unit1.eviction = False

unit2 = RentalUnit()
unit2.address = "60 Park"
unit2.rent = 3000
unit2.tenant_first = "Tom"
unit2.tenant_last = "Jones"
unit2.eviction = True

print(unit1.get_annual_rent())
print(unit2.get_annual_rent())