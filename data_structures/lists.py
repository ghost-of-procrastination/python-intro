cars = [
    'porsche 911',
    'bmw m8',
    'ferrari 296',
    'mclaren p1'
]

cars[3] = 'mclaren 720s'
print(cars[1:], '|', cars[1:3])

bikes = ['canyon spectral', 'yt jeffsy']

a = bikes.pop()
print(a, ': removed item using .pop()')
bikes.insert(1, 'specialized p.3')
bikes.remove('specialized p.3')
bikes.clear()
bikes.append('santa cruz v10')
bikes.sort()
bikes.reverse()
print(str(bikes.index('santa cruz v10')) + ': santa index |', str(bikes.count('santa cruz v10')) + ': santa count')

mixed = [*cars.copy()] + bikes.copy()

print(mixed, ': mixed copies')



