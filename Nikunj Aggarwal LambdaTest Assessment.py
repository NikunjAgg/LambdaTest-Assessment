# default dict is needed to make a dictionary with default or initial value as a list for each key
from collections import defaultdict  
import re  # for regex splitting

# Taking input as a string
inp = "samsung,'OEM Samsung Washing Machine Pulsator Washplate Cap Shipped With WA48J7700AW, WA48J7700AW/A2, WA48J7700AW/AA',20916,samsung,'OEM Samsung Chrome Washing Machine Washplate Pulsator Cap Shipped With WA52M7750AV, WA52M7750AV/A4, WA52M7750AW, WA52M7750AW/A4',91995,samsung, 'SAMSUNG Washing Machine Spring Hanger, DC61-01257M', 22970,samsung,'Samsung DC97-17022B Assy Detergent',32959,samsung,'Samsung DC66-00470A DAMPER SHOCK',29981,samsung,'DC64-00519D Samsung Washing Machine Door Lock Washer Dryer Dishwashe -MP#GH4498 349Y49HBRG9109150',52000,samsung,'Samsung DC97-16991A Assembly Filter',13000 "

# splitting input string  
inp = re.split(",(?=(?:[^']*\'[^']*\')*[^']*$)",inp)

#creating a default dictionary which will take value as a list for each key by default
d = defaultdict(list)


# for each 3 , separated strings we will create one key as those 3 belong to one product
for i in range(len(inp)):
    d[i//3].append(inp[i])
    
# creating another dictionary which will have values sorted by the price 
sorted_by_price = dict(sorted(d.items(), key=lambda value: int(value[1][2])))

# Now printing in the format as required
for i in sorted_by_price.values():
    print(','.join(i))
    print('')