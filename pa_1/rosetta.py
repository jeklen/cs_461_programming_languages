# PYTHON: Reverse-sort the lines from standard input
# execute:python rosetta.py < testcase.list> testcase.out
import sys          # bring in s standard library
lines = sys.__stdin__.readlines() # read every line from stdin into an array!
lines.sort(reverse = True)

for one_line in lines:
    print(one_line),    # the ending comma means "don't print another newline"

lines.sort()
for one_line in lines:
    print(one_line)
