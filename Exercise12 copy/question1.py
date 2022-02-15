#Create the cheese list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
#Add Oke to the end of the list using the append method (Append adds one value. Plus operator/ extend can be used to add multiple)
cheese.append('Oke')
#Add two cheeses in a single position using slice
cheese[3:3] = ['Oke', 'Mozzarella']
print(cheese)