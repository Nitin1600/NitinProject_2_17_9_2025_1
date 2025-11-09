from collections import Counter, OrderedDict

# l = [1,2,3,4,5,6,7,7,8,8,8,1,6,5,3,3,4,5]
# cnt=Counter(l)
# print(cnt)
# print(cnt[1])

# cnt=Counter({1:3, 2:4})
# print(list(cnt.elements()))
#
# l = [1,2,3,4,5,6,7,7,8,8,8,1,6,5,3,3,4,5]
# cnt = Counter(l)
# print(cnt.most_common())

# cnt = Counter({1:3, 2:4})
# print(type(cnt))
# deduct = {1:1, 2:2}
# print(type(deduct))
# cnt.subtract(deduct)
# print(cnt)

# cnt=Counter({1:3, 2:4})
# print(type(cnt))
# deduct={1:1, 2:2}
# print(type(deduct))
# cnt1 = cnt.subtract(deduct)
# print(cnt1)

# l = [4,5,6]
# l1 = l.reverse()
# print(l1)

# d={'id':2, 'name':'Raj'}
# print(d['id'])

# from collections import defaultdict
# d = defaultdict(str)
# d['id']=4
# d['name']='raj'
# print(d['address'])
# print(d['id'])

from collections import defaultdict

# count = defaultdict(int)
# names_list="Mike Anna Smith Britney Winnie Smith Britney Winnie Mike Jhon Anna Winnie Mike Anna Smith Britney Jhon Anna Smith Britney".split()
# print(names_list)
# for names in names_list:
#     count[names] += 1
# print(count)

from collections import OrderedDict
# od = OrderedDict()
# od['a']=1
# od["b"]=2
# od["c"]=3
# print(od)
# for key, value in od.items():
#     print(key, value)

# l = ["a", "b", "c", "c", "b", "a", "a", "c", "c", "b", "b", "c", "c", "b", "a", "b", "c", "c", "b", "a"]
# cnt = Counter(l)
# od = OrderedDict(cnt.most_common())
# for key, value in od.items():
#     print(key, value)

# from collections import deque
#
# l = ["a", "b", "c"]
# deq=deque(l)
# print(deq)
# deq.append("d")
# deq.appendleft("e")
# print(deq)
# deq.pop()
# deq.popleft()
# print(deq)
# print(deq.count())

# from collections import ChainMap
#
# dict1 = {"a":1, "b":2}
# dict2 = {"c":3, "b":4}
# chain_map = ChainMap(dict1, dict2)
# print(chain_map.maps)
# dict2["c"]=5
# print(chain_map.maps)
# dict3 = {"e":6, "f":7}
# new_chain_map = chain_map.new_child(dict3)
# print(new_chain_map.maps)

from collections import namedtuple

Student = namedtuple('Student', 'fname,lname,age')
s1 = Student('Jhon','Clarcke',18)
print(s1)
print(s1.fname)
s2 = Student._make(['Adams', 'Vandy', 21])
print(s2)
s2 = s1._asdict()
print(s2)
s2 = s1._replace(age=26)
print(s2)