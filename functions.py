FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath,"r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    :return:
    """
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

def delete_todos(delete_item):
    file = get_todos()
    for item in file:
        if item == delete_item:
            print(delete_item,9)
            file.remove(delete_item)
    write_todos(file)

if __name__ == "__main__":
    print(__name__)
    get_todos()
else:
    print(__name__)