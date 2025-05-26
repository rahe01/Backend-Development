a = frozenset([1,2,3,434,4,4])

initital_loc= id(a)


a= frozenset([2,3,4,4,45])

sec_loc = id(a)

print(initital_loc)
print(sec_loc)