try:
    file = open("forward.doc", "w")
    file.write("This is my file")

except IOError:
    print("Error: Can't find file or read data")
else:
    print("File created and writen successfully")
    file.close()

try:
    story = open("Tom and Jerry.txt","w")
    try:
        story.write("This is a very funny story line")
    finally:
        print("Successful. Closing file")
except IOError:
    print("Error: Can't find file or read data")