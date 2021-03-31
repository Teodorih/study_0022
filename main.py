print("Lab7 0022-04")
string = []
string2 = []
print("""
______________________________________________
Type in the list of line separated words.
Example: 
link 
site
force...
To leave the list press enter and type *q*
______________________________________________
""")
while (True):
    word = input("Your word: ")
    if (word[-1]) == 'q':
         break
    else:
         string.append(word)
string_set = set(string)
f = open('Lab7_text.txt', 'w')
print("Your quantity: ",string_set)
f.write("Your quantity: ")
f.write(str(string_set))
f.write("\n")
space = len(str(string).split())
print ("Your quantity contains",space,"words.")
f.write("Your quantity contains ")
f.write(str(space))
f.write(" words.")
f.write("\n")
lenth = str(string)
print("String lenth =",len(lenth)-(int(space)*4))
print("Type in new list of",len(lenth)-(int(space)*4),"symbols and same amount of words.")
for i in range(len(string)):
    word2 = input("Your word "+str(i+1)+": ")
    string2.append(word2)
d = {}
d = {string[i]:string2[i] for i in range(space)}
d = str(d)
f.write("Your dictionary: ")
f.write(d)
f.write("\n")
f.write("Your quantity contains ")
f.write(str(space))
f.write(" words and keys.")
f.write("\n")
f.close()
print("Your dictionary was successfully written to file Lab7_text.txt")
print(d)