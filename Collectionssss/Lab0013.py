from collections import Counter

# cnt = Counter()
# list=[1,2,3,4,5,6]
# Counter(list)
# Counter({1:3,2:4})
#
# list = [1,2,3,4,5,6,1,1,1,1]
# cnt=Counter(list)
# print(cnt[1])

# cnt=Counter({1:3,2:4})
# print(list(cnt.elements()))
# list=[1,2,3,4,5,6,5,4,3,2,2,2,3,4,5,6,1,2]
# cnt=Counter(list)
# print(cnt.most_common())

# cnt = Counter({1:3,2:4})
# deduct=({1:1,2:2})
# cnt.subtract(deduct)
# print(cnt)

# from collections import defaultdict
#
# nums = defaultdict(int)
# nums['one'] = 1
# nums['two'] = 2
# print(nums['three'])

# from collections import defaultdict
#
# count = defaultdict(int)
# names_list = "Anna Mike Smith Andrew Tyson Jhon Mike Smith Andrew Tyson Mike Smith Andrew Tyson Jhon Anna Mike Smith Mike Smith Andrew Tyson".split()
# for names in names_list:
#     count[names] += 1
# print(count)

# from collections import OrderedDict
#
# od = OrderedDict()
# od['a'] =1
# od['b'] =2
# od['c'] =3
# print(od)
#
# for key, values in od.items():
#     print(key, values)

# from collections import Counter
# from collections import OrderedDict
#
# list = ["a", "c", "c", "a", "b", "a", "c", "a", "b", "a", "c", "b", "c", "a", "c", "b", "c", "b",]
# cnt = Counter(list)
# od = OrderedDict(cnt.most_common())
# for key,  value in od.items():
#     print(key, value)

# from collections import deque
#
# list = ["a","b", "c"]
# deq=deque(list)
# print(deq)
#
# deq.append("d")
# deq.appendleft("e")
# print(deq)
# deq.pop()
# deq.popleft()
# print(deq)

from collections import deque

# list=["a","b","c"]
# deq=deque(list)
# print(deq)
# print(deq.clear())

list=["a","b","c"]
deq=deque(list)
print(deq.count("a"))
