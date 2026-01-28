tuple = ()

tuple_parents = ('jo', 'jane')
tuple_brothers = ('John', 'Mike', 'David')
tuple_sisters = ('Anna', 'Emma', 'Sophia')
tuple_siblings = tuple_brothers + tuple_sisters 
tuple_parents = tuple_parents

print("Siblings:", tuple_siblings)
print("Parents:", tuple_parents)
print("Number of siblings:", len(tuple_siblings))

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Nordic Countries:", nordic_countries)

print('Iceland' in nordic_countries)
print('Estonia' in nordic_countries)


all_items = tuple_siblings [3:4]

print(all_items)