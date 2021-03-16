import os


def Prettify(Path, file, extension):
    os.chdir(Path)
    list1 = os.listdir(Path)
    i = 1
    with open(file) as f:
        list_not_remove = f.read().split("\n")
    # print(list1)
    for j in list1:
        if j not in list_not_remove:
            if os.path.isdir(Path+r"/"+j):
                continue
            if os.path.isfile(Path+r"/"+j) and j.endswith(".txt"):
                os.rename(j, j.capitalize())
            if os.path.isfile(Path+r"/"+j) and j.endswith(".jpeg"):
                os.rename(j, f"{i}{extension}")
                print(i)
                i += 1
        else:
            continue


if __name__ == '__main__':
    # location = input("Enter the location: ")
    # file_name = input("Enter the file name: ")
    # extend = input("Enter the extension: ")
    Prettify("/Users/priyanshshukla/Downloads/python_os","/Users/priyanshshukla/Downloads/python_os/file1.txt",".jpeg")

