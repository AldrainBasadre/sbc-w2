log = True
while log:
    print("Choose: palindrome, box, diamond or stop to end")
    system = input("Enter: ").lower()
    
    #palindrome checker
    if system == "palindrome":
        w = []
        word = input("Enter a Palindrome Word: ")
        palindrome = word[::-1].replace(" ", "").lower()
        # palindrome = "".join(reversed(word.replace(" ", "").lower()))
        z = word.replace(" ","").lower()
        w.append(z)
        for i in w:
            if i == palindrome:
                print("palindrome")
            else:
                print("not a palindrome")
                
    #empty box
    elif system == "box":
        rows,cols = int(input("Enter Row: ")),int(input("Enter Column: "))
        i = 0
        while i < rows:
            if i == 0 or i == rows - 1:
                row = "*" * cols
            else:
                row = "*" + " " * (cols - 2) + "*"
            print(row)
            i += 1
            
    #updown pyramid
    elif system == "diamond":
        row = int(input("rows: "))
        for i in range(row, 1, -1):
            print("*" * i)
        for t in range(row-1):
            print("*" if t == 0 else " ", end="")
        print("*")
        for j in range(2,row + 1 ):
            print("*" * j)
    stop = log = False