
def count_words(filename):
    '''
    计算一个文件大概包含多少个单词
    '''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('No such file or directory: ' + filename)
    else:
        words = contents.split()
        # print(words)
        words_len = len(words)
        print('The file ' + filename + ' has about ' + str(words_len) + ' words')


# filename = 'alice.txt'
# filename = 'novel.txt'
filenames = ['alice.txt', 'novel.txt']

for filename in filenames:
    count_words(filename)