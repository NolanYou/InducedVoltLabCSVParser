import os
path = "C:/Users/Nolan/PycharmProjects/CSVParser"
# This is a sample Python script.
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
folders = []
rootdr = os.walk(path)
for root,subd,fils in rootdr :
    for name in fils:
        if name.endswith('.CSV'):
            folders.append(os.path.join(root, name))
folders.sort()
def readThree():

