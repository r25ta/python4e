def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_7/archives/"
    arq = open(path+"mbox.txt")
    for line in arq:
        line = line.rstrip()
        if not line.startswith("From "):
            continue
        words = line.split()
        print(words[2])
main()