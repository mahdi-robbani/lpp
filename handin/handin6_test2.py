#The handin6_test2.py file should be similar to handin6_test1.py, but now instead call the wordfile_differences_binary_search on the input files, and saves the result in a variable called differences. Again, use the timeit module to measure the time it takes to calculate the differences, and save this result in a variable called time_spent.
import handin6
import timeit

start_time = timeit.default_timer()
differences = handin6.wordfile_differences_binary_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time

