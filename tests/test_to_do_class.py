from lib.to_do_class import *

# add 'to do' tasks to empty list
def test_add_function():
    add = ToDoList()
    result = add.my_list("plan dinner")
    assert result == "plan dinner"
    assert "plan dinner" in add.tasks

# add 'to do' task to list with existing items

# hold an ongoing list of 'to do' tasks

# return a list of the stored tasks

# mark task a complete and remove