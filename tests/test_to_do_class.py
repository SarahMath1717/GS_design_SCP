from lib.to_do_class import *

# add 'to do' tasks to empty list
def test_add_function():
    add = ToDoList()
    result = add.my_list("plan dinner")
    assert result == ["plan dinner"]
    assert "plan dinner" in add.tasks

# add 'to do' task to list with existing items and hold an ongoing list of 'to do' tasks
def test_add_another():
    add = ToDoList()
    result = add.my_list("put on a load of washing")
    assert result == ["put on a load of washing"]
    result = add.my_list("get more eggs")
    assert result == ["put on a load of washing", "get more eggs"]
# return a list of the stored tasks

# mark task a complete and remove
def test_complete():
    add = ToDoList()
    result = add.my_list("put on a load of washing")
    assert result == ["put on a load of washing"]
    result = add.my_list("get more eggs")
    assert result == ["put on a load of washing", "get more eggs"]
    result = add.my_list("feed the snakes")
    assert result == ["put on a load of washing", "get more eggs", "feed the snakes"]
    result = add.complete(1)
    assert result == ["put on a load of washing", "feed the snakes"]