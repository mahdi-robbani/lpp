#In the module file called handin6.py, create a function called wordfile_to_list, which takes a single argument called filename. This function should read the file, and return a list with words. You can assume that each line in the file only contains a single word. Please remember to the remove newlines at the end of each line.
def wordfile_to_list(filename):
    '''Creates a list of words in the filename'''
    file = open(filename, "r")
    words = []
    for line in file: #traverses every line in the file
        words.append(line.strip()) #removes \n and adds files to a list
    return words

#Add a function to the handin6 module called wordfile_differences_linear_search, which takes two filenames as arguments, and calls wordfile_to_list to create a list for each of these files. The function should contain a loop that for each word in the first list looks through the second list to see if there is a match. It should return a list of words that are in the first file but not in the second file.
def wordfile_differences_linear_search(filename1, filename2):
    '''Creates a list of words found only in the first file, uses linear search'''
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_list(filename2)
    unique = []
    for i in word_list1:
        if i not in word_list2:
            unique.append(i)
    return unique

#It is much more efficient to find elements in a sorted list. One way of doing this is by using a method called binary search. Basically, binary search excludes half of the remaining list at every step of the search and will therefore only look at much fewer elements than the linear search above. To help you out, here is an implementation of a binary search function in Python:
def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False
def wordfile_differences_binary_search(filename1, filename2):
    '''Creates a list of words found only in the first file, uses binary search'''
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_list(filename2)
    unique = []
    for i in range(len(word_list1)):
        if binary_search(word_list2, word_list1[i]): # BETTER SOLUTION
            unique.append(word_list1[i])
        # if binary_search(word_list2, word_list1[i]): # Binary search returns True if match, so do nothing if search result is true
        #     continue
        # else:
        #     unique.append(word_list1[i]) # if search result is false, add word to list of unique words
    return unique

#Finally, we will test the speed of lookups in a Python dictionary. Create a function called wordfile_to_dict in the handin6 module. This function should be identical to wordfile_to_list, but save the results as keys in a dictionary rather than in a list (you can choose whatever you like for the values - for instance None).
def wordfile_to_dict(filename):
    '''Creates a dictionary where each key is a line from the file'''
    file = open(filename, "r")
    words_dict = {}
    for line in file:
        words_dict[line.strip()] = 1 # removes \n and adds word as dictionary key
    return words_dict

#Add a function to the handin6 module called wordfile_differences_dict_search, which takes two filenames as arguments, and calls wordfile_to_list on the first file and wordfile_to_dict on the second file. The function should contain a loop that for each word in the list looks in the dictionary to see if there is a match. It should return a list of words that are in the first file but not in the second file.
def wordfile_differences_dict_search(filename1, filename2):
    '''Creates a list with words found only in the first file, searches through a dictionary'''
    words_list1 = wordfile_to_list(filename1) #add stuff to list
    words_dict2 = wordfile_to_dict(filename2) # creates dictionary of second file
    differences = []
    for i in words_list1:
        if not i in words_dict2: ###### MUCH BETTER SOLUTION
            differences.append((i))
        # if i in words_dict2: # checks each key in list to find it in the dictionary, if matches, it does nothing
        #     continue
        # else:
        #     differences.append(i) # if no match is found, add key to list of differeneces
    return differences
