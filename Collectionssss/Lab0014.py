# from collections import ChainMap
#
# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'b':4}
# chain_map = ChainMap(dict1,dict2)
# print(chain_map.maps)
#
# print(chain_map['c'])
# dict2['c']=5
# print(chain_map.maps)

# from collections import ChainMap
#
# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'b':4}
# chain_map = ChainMap(dict1,dict2)
# print(list(chain_map.keys()))
# print(list(chain_map.values()))
# dict3={'e':5, 'f':6}
# new_chain_map=chain_map.new_child(dict3)
# print(new_chain_map.maps)

from collections import namedtuple

Student = namedtuple('Student', 'fname,lname,age')
s1 = Student('Jhon','Clarcke','18')
print(s1.fname)

s2 = Student._make(['Adams','Binny','22'])
print(s2)

s2 = s1._asdict()
print(s2)

s2 = s1._replace(age=25)
print(s1)
print(s2)