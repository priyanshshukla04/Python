s=set()
print(type(s))
s_from_list=set([1,2,'priyansh',3])
print(s_from_list)
#other way is
l=[1,2,3,4,5]
s_from_list=set(l)
print(s_from_list)
s1=set()
s1.add(1)
s1.add(1)   #again adding the same element in set will not add it
#print(s1)
a=s1.union({1,2})
print(a)
b=s1.intersection(a)
print(b)
#print(len(a))
#print(max(a))
#print(min(a))
s2={5,6}
print(s.isdisjoint(s2))
s1.remove(1)
print(s1)