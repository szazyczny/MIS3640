import os
print(os.getcwd())

fout = open('session14/output.txt', 'a')

line1 = "How many roads must a man walk down\n"
fout.write(line1)
line2 = "Before you call him a man?\n"
fout.write(line2)
fout.close() # must close

print(os.path.abspath('session14/output.txt'))

# check to see if file exists
print(os.path.exists('session14/output.txt')) # true
print(os.path.exists('session14/input.txt')) # false 


# Filenames and paths
# To demonstrate these functions, the following example “walks” through a 
# directory, prints the names of all the files, 
# and calls itself recursively on all the directories.
def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path) # recursive


# Catching exceptions
fin = open('bad_file')

# try and expect runs whole code, does not stop when finds error
try:    
    fin = open('bad_file')
except:
    print('Something went wrong.') # if there is a problem try to find it

folder = os.getcwd # get current folder in working directory
walk(folder)

# cannot do
# a = [1, 2, 3]
# try:
#     print(a[1.5])
# except:
#     print('Something is wrong.')


# Pickling
# import pickle
# t = [1, 2, 3]
# print(pickle.dumps(t))

# t1 = [1, 2, 3]
# s = pickle.dumps(t1)
# t2 = pickle.loads(s)
# print(t2)

# t1 == t2

# t1 is t2


import pickle

t1 = [1, 2, 3] # t1 is saved .p

# f = open('save.p', 'wb')
# s = pickle.dump(t1, f) # dump list to save.p
# f.close()

t2 = pickle.load(open('save.p', 'rb')) # rb means reads bytes
print(t2)

print(t1 == t2) # true
