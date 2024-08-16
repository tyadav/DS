# To find compound interest 
 
# inputs 
p= 1400000   # principal amount 
t= 5      # time 
r= 10.5   # rate 
# calculates the compound interest
a=p*(1+(r/100))**t  # formula for calculating amount 
ci=a-p  # compound interest = amount - principal amount
# printing compound interest value
print(ci)