
import os

f1 = open("hbta.txt", "r+")

f2 = open("happy.txt", "w")


for lines in f1:
    text = "printf(\""+lines+"\\n\"a;\n"
    f2.write(text+"\n")

f1.close
f2.close
# f = open("text.txt", "r")
# for x in f:
#   print(x)
