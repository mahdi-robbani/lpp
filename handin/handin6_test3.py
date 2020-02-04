#The test code in handin6_test3.py should be similar to the two others, but now call the wordfile_differences_dict_search on the input files. Again you should save the result in a variable called differences and the timeit module to measure the time it takes to do the calculation, and save this result in a variable called time_spent.
import handin6
import timeit

start_time = timeit.default_timer()
differences = handin6.wordfile_differences_dict_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time

