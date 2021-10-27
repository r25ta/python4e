import os

def main():
    for root, dirs, files in os.walk("/home/ronaldo/_DESENVOLVIMENTO/Python"):
        for file_name in files:
            print(os.path.join(root, file_name))
            print(file_name)
            
        for dir_name in dirs:
            print(os.path.join(root,dir_name))
            print(dir_name)
            
main()