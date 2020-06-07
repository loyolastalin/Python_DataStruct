a = set([1,2,3,3])
b = {1, 2,4}
z  = a.intersection(b)
diff  = a.difference(b)
sumy  = a.symmetric_difference(b)
print(z,diff, sumy)

employee = ['stalin', 'loyola', 'soosai']
gym = ['stalin']
microsoft_dev = ['stalin','loyola']

# get all the employee going to gym and microsft developper

result  = set(gym).intersection(microsoft_dev)
print(result)

# gey all the employee not going to gym nor microsoft developper
result1  = set(employee).difference(gym, microsoft_dev)
print(result1)