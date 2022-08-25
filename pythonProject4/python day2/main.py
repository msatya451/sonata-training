from leave import Leave
from basketleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22790,"satya",20,"2001-06-14")
print(r1.display_dob())
b1=BasketOfLeave(22790,"satya",20,1)
print(b1.display())
