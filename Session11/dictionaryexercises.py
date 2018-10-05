#DICTIONARIES

#Exercise 1
#Rewrite function histrogram using get. 
#You should be able to eliminate the if statement.
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

def histogram(s):
    d = dict()
    for c in s:
        return d.get(c)

h = histogram('Bookkeeper')
print(h)

# number_of_e = h.get('e', 0)
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)




