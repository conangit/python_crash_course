
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('No such file or directory')
else:
    print(contents)

filename = 'novel.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('No such file or directory')
else:
    words = contents.split()
    # print(words)
    words_len = len(words)
    print('The file ' + filename + ' has about ' + str(words_len) + ' words')