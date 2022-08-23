def counter(file):
    count = 0
    text = ""
    word = "ey"

    for i in file:
        text = i
        count = count + text.lower().count(word)

    return count


def openFile():
    file = open("msg.txt", "r")
    return file


f = openFile()
print(counter(f))
