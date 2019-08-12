dict1={'a':1,'b':2,'c':3,'e':4,'f':5}
rem_item={'a','e','f'}
print('The original list is:',dict1)
[dict1.pop(key) for key in rem_item]
print('After removal of items:',dict1)
