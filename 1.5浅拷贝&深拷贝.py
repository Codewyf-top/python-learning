import copy
a = [1,2,[1,2]]
b = a
c = copy.copy(a) #浅拷贝 使用copy()函数，拷贝了list最外围，而list内部的对象仍是引用。
d = a[:]         #相当于浅拷贝，与c相同
e = copy.deepcopy(a)  #深拷贝，使用了deepcopy()函数，list内外围均为拷贝，因此前后的变量完全隔离，而非引用
a.append(3)
print(a)
print("__________-_____")
a[2].append(3)
print(a)
print(b)
print(c)
print(d)
print(e)