# Tupple and list

# L = [1, 2, 3, 4, 5, 0 ]#list mutable=changeable
# T = (1, 2, 3, 4, 5, 0 )#tupple immutable=unchangeable

# L[5] = 6
# L.append(7)

# # print(L[1:4])
# # print(T[1:4])

# print(L)
# print(T)

######################################

# l = [5,4,7,1,2]
# print(l[0])

# l.append(3)
# l.append("3")
# l=[]
# x = input("Enter a list: ")
# l.append(x)#sa last add
# l.insert(1,6)#ikaw buot aha dapit i add
# l[2] = 3 #replace in a list
# l.remove(5)#remove by value
# l.pop()#remove by index
# l.clear()
# l.sort() #sort the list
# l.sort(reverse=True) #sort first then reverse
# l.reverse() #reverse the list
# print(len(l))

#stack[LIFO] = last in first out
#Queue[FIFO] = First in first out

# l = []
# #append
# l.append("handle")
# l.append("blade")
# l.append("point")
# print(l)
# #insert
# l.insert(0,"sword")
# l.insert(1,"spear")
# l.insert(2,"bow")
# print(l)
# #remove
# l.remove("bow")
# print(l)
# #pop
# l.pop()
# print (l)

#*********************************************
#activity

# while True:
#     l = []#list
    
    #making a list
    #1
    # x,y,z,n,m = input("enter list: "),input("enter list: "),input("enter list: "),input("enter list: "),input("enter list: ")
    # l.append(x),l.append(y),l.append(z),l.append(n),l.append(m)
    #2
    # for i in range(3):
    #     x = input(f"enter value in list {i+1}: ")
    #     l.append(x)   
    #3
    # thelist = [int(input(f"({list}enter list: ")) for list in ["","","","",""]]
    # l.append(thelist)
    
    #printing the list
    # print("the list are: ",l)
    # print("the list are: ",thelist)
    
    #asking for condition
    # print ("0 if naa 1 if wla")
    # b = int(input("is boss here?: "))
    
    #condition for dropping a value in list
    # if b == 0:
        # l.pop(0)
        # l.sort()
        # print ("display result: ", l)
    #     thelist.pop(0)
    #     thelist.sort()
    #     print ("display result: ", thelist)
    # elif b == 1:
        # l.pop()
        # print("display result: ", l)
    #     thelist.pop()
    #     print("display result: ", thelist)
    # else:
    #     print ("idk".upper())
        
    # stop = input("wanna make a list?(yes/no)")
    # if stop != "yes":
    #     break

#**************************************

# array    
# arr = (
#     [1,2,3],
#     [4,5,6]
#     )
# print(arr[1])
# print(arr[1][2])
#dictionary
# d = {"me":"ako",
#     "stone":"cold",
#     "war":"hitler",
#     "gun":["pistol","smg","ar","mg"]
#     }
# print(d["me"])
# print(d["war"])
# print(d["gun"])
# print(d["stone"])
#***********************************************
# data = [["Aldrain","M.","Basadre","30"],
#         ["unknown","idk","dunno","150"]]

# final = []

# for d in data:
#     label = {}
#     label["firstname"] = d[0]
#     label["middlename"] = d[1]
#     label["lastname"] = d[2]
#     label["age"] = d[3]
#     final.append(label)
# print (final)

###########################################
#d2
###########################################
# m = 0
# while m < 5:
#     print("weeee")
#     m += 1

#h = ["Hello World", "Thank you God", "God Bless", "Good Bye",]

# for char in h: #pwede num,variable and string
#     print(char)

# m = int(input("row: "))

# for n in range(m + 1):
#     print("*" * n)

###

# n = int(input("How old are you?:"))
# while n >= 18 :
#     print(":>".format())
#     break
# else:
#     print(":< jail time".format())

#########

# log = True

# while log:
# while True:
#     username = input("Username: ").strip()
#     password = input("Password: ").strip()
#     if username == "blade" and password == "sword":
#         print("Login Successfully")
#         # log = False
#         break
#     else:
#         print("Try Again")
################
#activity
# log = True
# while log:
#     print("Choose: palindrome, box, diamond or stop to end")
#     system = input("Enter: ").lower()
#     if system == "palindrome":
#         w = []
#         word = input("Enter a Palindrome Word: ")
#         palindrome = word[::-1].replace(" ", "").lower()
#         # palindrome = "".join(reversed(word.replace(" ", "").lower()))
#         z = word.replace(" ","").lower()
#         w.append(z)
#         for i in w:
#             if i == palindrome:
#                 print("palindrome")
#             else:
#                 print("not a palindrome")
#     elif system == "box":
#         rows,cols = int(input("Enter Row: ")),int(input("Enter Column: "))
#         i = 0
#         while i < rows:
#             if i == 0 or i == rows - 1:
#                 row = "*" * cols
#             else:
#                 row = "*" + " " * (cols - 2) + "*"
#             print(row)
#             i += 1
#     elif system == "diamond":
#         row = int(input("rows: "))
#         for i in range(row, 1, -1):
#             print("*" * i)
#         for t in range(row-1):
#             print("*" if t == 0 else " ", end="")
#         print("*")
#         for j in range(2,row + 1 ):
#             print("*" * j)
        
#     stop = log = False