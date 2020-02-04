#Create a function called read_data, that takes a filename as argument. The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values, and append them to an outer list). The function should return this list. Test the function by calling it on the experimental_results.txt file like this:
def read_data(filename):
    """Loads file into list, creates an index which will be used to index each line in the file, coverts each string to a float"""
    file = open(filename, "r")
    list_of_rows = []
    #index_i = 0
    for line in file:
        number = line.split()
        number_float = [float(number[0]), float(number[1])]
        list_of_rows.append(number_float)
        #list_of_rows.append(line.split()) # converts each row into a list of two items (still strings)
        #for j in range(len(list_of_rows[index_i])): #traverse inner list
        #   list_of_rows[index_i][j] = float(list_of_rows[index_i][j]) #convert strings to float
        #index_i+=1
    return list_of_rows
list_of_rows = read_data("experimental_results.txt")
print(list_of_rows)

#Write a function called calc_averages that takes a list of list of floats as input, and calculates the average value for each column by iterating over the rows. The function should return these two values. Test the function by calling it like this:
def calc_averages(list_of_rows):
    """Create sum of column 1 and column2, divide by length of column to get average"""
    sum_col1 = 0
    sum_col2 = 0
    for i in range(len(list_of_rows)): #traverse list and add values of each column to the respective sum
        sum_col1 += list_of_rows[i][0]
        sum_col2 += list_of_rows[i][1]
    return sum_col1/len(list_of_rows), sum_col2/len(list_of_rows)
col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)

#Write a function called transpose_data that turns the list of lists around so that it becomes a list of columns, rather than a list of rows. This means that the outer list now has two elements each containing a list of all the values in the corresponding column. In other words, if I want to access the 26th value in the 2nd column, I would now index with [1][25] instead of [25][1]. Hint: Note that these two nested lists are just two different ways of representing the same table of data. Here is a sketch of the two variants:
def transpose_data(list_of_rows):
    "Create 2 empty lists, insert every value from column 0 into list 0 and every value from column 1 into list 1, put both lists in another list"
    list_0 = []
    list_1 = []
    for i in range(len(list_of_rows)): #traverse though list and append each value to respective list
        list_0.append(list_of_rows[i][0])
        list_1.append(list_of_rows[i][1])
    list_c = [list_0, list_1] #make list of lists
    print(list_0, list_1)
    return list_c
list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)
