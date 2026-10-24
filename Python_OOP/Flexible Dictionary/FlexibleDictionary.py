class FlexibleDictionary(dict):

   def __getitem__(self, key):
       if isinstance(key,str) and key.isdigit():
           key=int(key)
       return super().get(key)
my_dict=FlexibleDictionary({1:"value"})
print(my_dict[1])
print(my_dict['1'])







