class ToDoList():
    def __init__(self):
        self.tasks = []

    def my_list(self, task):
        self.tasks.append(task)
        return self.tasks
    
    def complete(self, completed):
        self.tasks.pop(completed)
        return self.tasks