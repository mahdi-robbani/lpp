import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#1.2 Now we will process the data in Python. Inside the exam.py file, write a function called read_year_to_anomaly_data that takes a single argument: a filename. The function should open the file, iterate over the entries using a for loop and extract the first two columns of the file (containing the year and temperature anomaly). The function should return a dictionary, in which the years are keys (integers) and the temperature anomalies are values (floats).
def read_year_to_anomaly_data(filename):
    '''Reads an input file and creates a dictionary where the keys are years, and the values are anomalies'''
    file = open(filename, "r")
    year_anomaly_dict = {}
    for i in file:
        if i[0] != "%" and len(i) > 2: #skips all comments and the first blank line
            i = i.split() # split line into lists
            year_anomaly_dict[int(i[0])] = float(i[1]) # create dict
    file.close()
    return year_anomaly_dict

#1.3 We now wish to create a simple line plot with years on the x-axis and temperature anomalies on the y-axis. Copy the following code to your exam.py as a starting point. Replace the # YOUR CODE HERE line with code that creates such a line figure (using the plot function), and saves the result to the filename specified by the function argument. Import the necessary external modules to make it work.
def create_line_plot(data, out_filename):
    '''Creates line plot of the key,value pairs in the dictionary'''

    fig, ax = plt.subplots()

    #add labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Global Temperature Anomaly')
    ax.set_title('Annual Global Temperature Anomaly')

    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y) #plot figure
    plt.savefig(out_filename)       #save figure

    return fig, ax

#2.1 Within the exam.py file, create a ColorMapper class with a constructor that takes two arguments: 1) values: a list of temperatures, and 2) cmap_str: a string with a name of matplotlib color map object, which should default to "RdBu_r". The constructor should define two attributes in the object it is creating: 1) max_abs_value, which contains the maximum absolute value of the temperature anomalies, and 2) cmap, which is the underlying matplotlib colormap function (the object you get when calling get_cmap as described above).
class ColorMapper:
    def __init__(self, values, cmap_str="RdBu_r"):
        '''Constructor'''
        abs_value = 0
        for i in values:
            if abs(i) > abs_value: # take absolute value from every item in and replace the variable if the new value is larger
                abs_value = abs(i)
        self.max_abs_value = abs_value # create max value attribute
        self.cmap = plt.get_cmap(cmap_str) # create cmap attribute

    def get_color(self, temperature):
        '''Normalizes the temperature and calls cmap on it'''
        normalized_temp = (temperature+self.max_abs_value)/(self.max_abs_value+self.max_abs_value)  # normalized value
        return self.cmap(normalized_temp)

#2.2 We will now create the function to create the vertical stripes. Write a function called construct_blocks that takes three arguments: 1) data: a dictionary with (year, temperature anomaly) values, 2) bottom: a value specifying the lower coordinate value of each stripe, which should default to 0.0, and 3) height: a value specifying the height of each stripe, which should default to 1.0. The function should return a list of tuples, each with 5 elements: (year, bottom, width, height, temperature anomaly), where width is the width of the stripe, measured in years, which we can just set to 1.
def construct_blocks(data, bottom=0.0, height=1.0):
    '''takes in a dictionary ad returns a list of tuples where the first item in the tuple is the dict key and the last item is the dict value'''
    list_of_tuples = []
    for i in data:
        tuple_i = (i, bottom, 1, height, data[i])
        list_of_tuples.append(tuple_i)
    return list_of_tuples

def plot_blocks(list_of_blocks, color_mapper,
                colorbar=True,
                figure_width=20, figure_height=5):
    '''
    Visualize list of blocks, where each block is specified in the format
    (x-coordinate, y-coordinate, width, height, value). The color_mapper is
    used to look up colors corresponding to the values provided in each block.

    :param list_of_blocks: List of (x-coordinate, y-coordinate, width, height, value) tuples
    :param color_mapper: Used to lookup values for each block
    :param colorbar: Whether to include a color bar
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return: None
    '''

    fig, ax = plt.subplots(1, figsize=(figure_width, figure_height))
    x_values = []
    y_values = []
    for block in list_of_blocks:
        rect = matplotlib.patches.Rectangle(block[:2], block[2], block[3],
                                            linewidth=1, edgecolor='none',
                                            facecolor=color_mapper.get_color(block[-1]))
        ax.add_patch(rect)
        x_values += [block[0], block[0]+block[2]]
        y_values += [block[1], block[1]+block[3]]

    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(plt.gca())
        ax_cb = divider.new_horizontal(size="1%", pad=0.1)
        matplotlib.colorbar.ColorbarBase(ax_cb, cmap=color_mapper.cmap,
                                         orientation='vertical',
                                         norm=matplotlib.colors.Normalize(
                                             vmin=-color_mapper.max_abs_value,
                                             vmax=color_mapper.max_abs_value))

    #add labels
    ax.set_xlabel('Year')
    ax.set_title('Annual Global Temperature Anomaly')

    plt.gcf().add_axes(ax_cb)
    plt.show()

#2.3 To summarize the data in another way, we will now calculate the average anomaly per decade. Inside the exam.py file, write a function called calculate_anomalies_per_decade that takes a dictionary of (year,anomaly) values as input. The function should return a new dictionary, where the keys are (start,end) tuples (e.g. (1950,1960)) and the values are the average anomalies for that period of time. A decade should include the start-year of the period, but exclude the end-year (i.e. (1950,1960) does not include the year 1960). If a decade is incomplete, the average should be over the available years, and the key should be adjusted accordingly (e.g. (2010,2019), when data for 2019 is missing).
def calculate_anomalies_per_decade(dict):
    '''Takes a dictionary and returns a new dictionary of a tuple {(start, end) : average from start to end values}'''
    dict_out = {}
    years = list(dict.keys())
    sum = dict[years[0]]            #initililize sum value
    start = years[0]                #initialize start year
    for i in range(1, len(years)):      #skip first year
        if years[i] == years[-1]:       #for last year in list
            end = years[i] + 1          # add extra year because question asks end of tuple to be 2019 if data ends at 2018
            sum += dict[years[i]]
            average = sum/(end-start)
            dict_out[(start, end)] = average    #create dictionary entry
        elif years[i] % 10 != 0:        #if years are not divisible by 10, keep adding to sum
            sum += dict[years[i]]
        elif years[i] % 10 == 0:        #if years are divisible by 10
            end = years[i]
            average = sum/(end-start)
            dict_out[(start, end)] = average    #create dict
            sum = dict[years[i]]        #reset sum
            start = end                 #set new start year
    return dict_out

#3.1 In exam.py, write a function called read_latitude_year_to_anomaly_data. The function should take a single filename as argument, and return a dictionary of dictionaries, such that the outer dictionary has latitudes (floats) as keys, and the inner dictionaries have years as keys (integers) and anomalies as values (floats).
def read_latitude_year_to_anomaly_data(filename):
    '''Creates a dictionary of dictionaries with the structure {latitude1 : {year1 : anomaly1, year2:anomaly2}, latitude2 : {year1 : anomaly1, year2:anomaly2} '''
    file = open(filename, "r")
    outer_dict = {}
    for i in file:
        i = i.split()       #split line into lists
        year = int(i[0])        #convert from string to int/float
        anomaly = float(i[2])
        latitude = float(i[1])
        if latitude not in outer_dict:      #if outer dict is empty, crete the values for latitude
            outer_dict[latitude] = {year:anomaly}
        else:                                  #else append the value so previous values already in the outer dict are not replaced
            outer_dict[latitude].update({year:anomaly})
    file.close()
    return outer_dict

#3.2 Since we now have a nested dictionary, we cannot easily access all values at once. In the exam.py file, write a function called get_values_from_nested_dict that takes a nested dictionary as input, and returns a list of all values contained in all the sub-dictionaries (in our case, the temperature anomalies at any latitude value).
def get_values_from_nested_dict(nested_dict):
    '''Takes in a nested dictionary and returns all values'''
    list_of_anomalies = []
    for i in nested_dict:           #traverses outer dict
        for j in nested_dict[i]:    #traverses inner dict
            list_of_anomalies.append(nested_dict[i][j])
    return list_of_anomalies

#Part 3.3 Rather than the long vertical stripes that we plotted in Part 2, we will now use the vertical dimension of the visualization to reflect the latitude (so the top of the image corresponds to the north pole and the bottom of the visualization corresponds to the south pole). Write a function called construct_latitude_blocks that takes a single argument: a dictionary of dictionaries as we have just created in the previous exercise. Similar to the construct_blocks function, this function should return a list of tuples, each with 5 elements: (year, latitude, width, height, temperature anomaly), where width is the width of the stripe, measured in years, which we can just set to 1. The height of each block should be the height of the latitude band: 5 degrees. If you want, you can simplify your code by calling the construct_blocks function from within this function, but this is entirely optional.
def construct_latitude_blocks(nested_dict):
    '''Takes in a nested dict and for every dict in the outer dict, calls the contruct_blocks function and creates a list of tuples'''
    list_of_tuples = []
    for i in nested_dict:   #traverse outer list
        for j in range(len(nested_dict[i])):        #traverse inner list
            list_of_tuples.append(construct_blocks(nested_dict[i], i, 5)[j])         #crreate list of tuples
    return list_of_tuples

#4.2 We'll now do the same in Python. In the exam.py file, write a function called find_top10_emitting_countries that takes a filename as argument. The final result should be a list of the 10 highest emitting countries (i.e. entries with a 3-letter country code) in the most recent year, sorted by their CO2 emission. The function should return a list of (full country name, CO2 emission) tuples.
def find_top10_emitting_countries(filename):
    '''Takes a filename as input and returns a list of tuples containing the country names and emissions'''
    file = open(filename, "r")
    list_of_entries = []

    def sort_key(list):         #used to sort list by 3rd and 4th value
        return list[2:4]

    for i in file:
        i = i.rstrip().split(",")
        if i[0] == "Entity" or len(i[1]) != 3:  #skip the first line and lines that do not have a country code
            continue
        else:
            i[2] = int(i[2])           #convert year value to int
            i[3] = float(i[3])         #convert emission to float
            list_of_entries.append(i)   #create list of all entries in file
    file.close()

    list_of_entries.sort(key=sort_key, reverse=True)        #sort the list of all entries
    list_of_tuples = []
    for i in list_of_entries[0:10]:     #for only the first 10 entries in the file (these have max emissions)
        country = i[0]
        emission = i[3]
        tuple = (country, emission)        #create a tuple of countries and emissions
        list_of_tuples.append(tuple)        #add tuple to a list
    return list_of_tuples

def plot_emissions(list_of_tuples, population_dict=None, figure_width=15, figure_height=5):
    '''
    Create a bar plot of CO2 emissions. If population_dict is provided, resize
    bars so that width reflect population size and height denotes emission per
    capita.

    :param list_of_tuples: List of (country-name, value) tuples
    :param population_dict: Dictionary of (country-name, population) pairs
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return:
    '''

    # Create new figure
    fig,ax = plt.subplots(1, figsize=(figure_width, figure_height))

    # Choose color map
    cmap = plt.get_cmap("Spectral")

    heights = []
    labels = []
    widths = []
    colors = []
    for i, entry in enumerate(list_of_tuples):
        heights.append(entry[1])
        # Scale down height of bar with population size
        if population_dict is not None:
            heights[-1] /= population_dict[entry[0]]
        labels.append(entry[0])
        colors.append(cmap(i/len(list_of_tuples)))
    if population_dict is None:
        x = range(len(list_of_tuples))
        widths = [0.9] * len(list_of_tuples)
    else:
        max_width = 0
        for entry in list_of_tuples[:-1]:
            max_width = max(max_width, population_dict[entry[0]])
        x = np.arange(len(list_of_tuples)) * max_width
        for entry in list_of_tuples:
             widths.append(population_dict[entry[0]])

    # Create bar plot and set tick values
    plt.bar(x, height=heights, width=widths, color=colors)
    plt.ylabel("Annual CO2 emissions (tonnes)")
    ax.set_title('Top 10 CO2 emitting countries in the world')
    plt.xticks(x, labels, rotation=45, ha="right")
    plt.show()

#4.3 In addition to comparing CO2 emissions by country, we also want to compare it by how much each individual person in these countries contribute (CO2 emission per capita). To do this, we need to read in population size data. In your exam.py file, write a function called read_population_data that takes two arguments: a filename and a year-value. The function should return a dictionary with country/region names as keys, and population sizes (at the given year) as values.
def read_population_data(filename, year):
    '''Returns a dictionary of countries with their populations'''
    file = open(filename, "r")
    year = str(year)
    pop_dict = {}
    for i in file:
        i = i.rstrip().split(",")       #remove \n and splits file into lists
        if i[0] == "Entity" or len(i[1]) != 3 or i[2] != year:      #removes the first line, blank lines and all years that are not specified
            continue
        else:
            country = i[0]
            population = int(i[3])
            pop_dict[country] = population      #creates a {country: population} dictionary
    file.close()
    return pop_dict

print(find_top10_emitting_countries("data/annual-co-emissions-by-region.csv"))
print(read_population_data("data/population.csv", 2017))
