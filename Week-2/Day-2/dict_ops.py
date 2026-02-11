words = {
    'a': "apple", 
    'b': "ball", 
    'c': "cat"
    }
print("Words:")
print(words)

print("\nAdding word in dictionary:")
words['d'] = "dog"
words['e'] = "egg"
print(words)

print("\nRemoving word from dictionary:")
words.pop('c')
words.pop('e')
print(words)

print("\nUpdating word in dictionary:")
words.update({'a': 'ant'})
words['d'] = "dragoan"
print(words)
