#Write a function that will find the second largest in a list
from time import time

def basic_list(list1):
    pass

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

@timer_func
def matching_words(string1, other_strings):
    string1 = string1.lower()
#Find all of the 5 word combinations in string1
    string1 = string1.split()

    for current_length in range(len(string1)-1, 0, -1):
        for start_position in range(len(string1)-current_length -1):
            words = string1[start_position:start_position + current_length]
            words = ' '.join(words)
            for string in other_strings:
                if words in string.lower():
                    return words

@timer_func
def matching_letters(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
#Find all of the 5 word combinations in string1

    for current_length in range(len(string1)-1, 0, -1):
        for start_position in range(len(string1)-current_length -1):
            letters = string1[start_position:start_position + current_length]
            if letters in string2:
                return letters

def get_longest_matching_words(filename1,other_files):
    other_strings = []
    file1  = open(filename1, 'r')
    string1 = file1.read()
    for file in other_files:
        file2 = open(file, 'r')
        string2 = file2.read()
        other_strings.append(string2)
    return matching_words(string1, other_strings)