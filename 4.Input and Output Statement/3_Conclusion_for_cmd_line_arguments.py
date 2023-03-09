# Conclusion abt cmd line arguments.
from sys import argv

# case 1
# python3 3_Conclusion_for_cmd_line_arguments.py Sunny Leone

print('Value at index 1 in argv :- ',argv[1]) # it will peak 1st value index seprated by space.

# case 2
# python3 3_Conclusion_for_cmd_line_arguments.py "Sunny Leone"

print('Value at index 1 in argv :- ',argv[1]) # value in single , double coat will be consider as value for index 1.

# case 3
# python3 3_Conclusion_for_cmd_line_arguments.py 10 20
print('concatination :- ',argv[1] + argv[2]) # All command line arguments are considered as string.
print('Sum :- ',int(argv[1]) + int(argv[2]))

# python3 3_Conclusion_for_cmd_line_arguments.py 10 20 30 
# print(argv[100]) => out of range index will give error.

