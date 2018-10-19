# Writing modules

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('Session14/wc.py'))

# to import the module
# able to use function in powershell
# python wc.py
# import wc
# use wc.linecount