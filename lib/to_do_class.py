class ToDoList():
    def __init__(self):
        self.tasks = []

    def my_list(self, task):
        self.tasks.append(task)
        return task
        