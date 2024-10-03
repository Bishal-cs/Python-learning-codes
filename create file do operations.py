'''create a new file "practice.txt", add the following data in it :
"Hi everyone" \n "we learning file I/O" \n "using Java" \n "I like programming in Java", 
Replace "Java" with "Python"
Find Learning in this file define a function. And find the line number.'''

with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe learning file I/O")
    f.write("\nusing Java \nI like programming in Java")   # write some what you want 
    
with open("practice.txt","r") as f:
    data = f.read()
    print("Old data is---------\n",data)
    New_data = data.replace("Java", "Python")
   
with open("practice.txt","w") as f:
     f.write(New_data)
     print("New data is---------\n",New_data)
    
def find_word():
    word = input("Enter data for search: ")
    with open("practice.txt","r") as f:
        f_word = f.read()
        if (f_word.find(word) != -1):
            print("I find this data:")
        else:
            print("Data is not foun in this file.")
find_word()

def find_line():
    word = input("Enter the word to find the line: ")
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
        return -1
find_line()
    
