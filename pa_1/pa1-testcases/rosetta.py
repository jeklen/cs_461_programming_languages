# PYTHON: Reverse-sort the lines from standard input
# execute:python rosetta.py < testcase.list> testcase.out
import sys          # bring in s standard library
lines = sys.__stdin__.readlines() # read every line from stdin into an array
# 假设输入的就是有向无环图
# lines.sort(reverse = True)
# 新建一个数组，每一个元素都是不同的
# 再建一个字典，key为每个不同的行，value为在上述数组里头的标号
index = 0
dic = {}
li = []
for line in lines:
    if line not in dic:
        dic[line] = index
        index = index + 1
        li.append(line)
# graph stand for the list of the list of each node
# create a list of empty list


print("***************************\n")
for one_line in lines:
    print(one_line),    # the ending comma means "don't print another newline"
