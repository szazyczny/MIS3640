# open existing file
# open empty file
# read existing file to find word to replace
# update and put in new file
def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source = open(source, 'r')
    f_dest = open(dest, 'w') # destination file

    for line in f_source:
        new_line = line.replace(pattern, replace)
        f_dest.write(new_line)

    f_source.close()
    f_dest.close()
# dont forget to close!

pattern = ' man '
replace = ' woman '
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)

# pattern = 'Jude'
# replace = 'Jack'
# source = 'sed_tester.txt'
# dest = 'new_' + source
# sed(pattern, replace, source, dest)