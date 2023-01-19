#Write a function that will find the second largest in a list
from time import time
#pass ignores the function
def basic_list(list1):
    pass
#1nd method
    # list1.sort()
    # return list1[-2]

#2nd method    
    # largest = max(list1)
    # list1.remove(largest)
    # return max(list1)
    
# list1 = [1,-3,100,1000,500]
# print(basic_list(list1))

#How long does it take this function to run?
#Sorting takes a lot of time.  Move lots of data around.  Overkill for a basic scenario.

#Given two strings, find if there is a sequence of at least 5 words in both strings
#Use case: checking for plagiarism.

#Create a fuction that takes in two variables
#define the string
#loop through the words until you find a match
#return the results

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
#range what variable starts.  -1 changes will decrease by 1.
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
    # for i in
    for current_length in range(len(string1)-1, 0, -1):
        for start_position in range(len(string1)-current_length -1):
            letters = string1[start_position:start_position + current_length]
            if letters in string2:
                return letters
#abcde - This is all the letters of our str1, using a string splice ':'.

#Never define parameters in the function, defeats the purpose.  
# string1 = "The quick brown blue dark fox jumped over the lazy dog fence"
# string2 = "Whales are really big and the quick brown blue dark fox jumped past everything and it was marvelous!"
def get_longest_matching_words(filename1,other_files):
    other_strings = []
    file1  = open(filename1, 'r')
    string1 = file1.read()
    for file in other_files:
        file2 = open(file, 'r')
        string2 = file2.read()
        other_strings.append(string2)
    return matching_words(string1, other_strings)

# result = get_longest_matching_words('plag_sample1.txt','plag_sample2.txt')
# print(result)