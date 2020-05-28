'''Create a TODO application in python using sqllite3'''

import sqlite3 as sql3

class TODO:
    """To-do class to store and retrieve data from the sqllite-3 database"""
    max_priority = 10
    def __init__(self):
        """Initialize database and create table if don't exists"""
        self.conn = sql3.connect("todo-tasks-sqllite3.db")
        self.db_cursor = self.conn.cursor()
        self.create_table_if_not_exists()

    def __del__(self):
        """Close the DB connection when the object goes out of scope"""
        self.conn.close()

    def create_table_if_not_exists(self):
        """Create table when it doesn't exists"""
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            priority INTEGER NOT NULL);''')

    def add_task(self, task_name, task_priority):
        """add tasks by validating the input parameter by inserting data into sqllite3"""
        try:
            if len(str(task_name).strip()) <= 0:
                print("Empty task names can't be used to add tasks")
                raise ValueError
            if task_priority > self.max_priority:
                print("Priority should be less than {0}".format(self.max_priority))
                raise ValueError
            if self.find_tasks(task_name):
                print("The tasks are alreay existing, please use different name")
                raise ValueError
            self.db_cursor.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', \
                                   (task_name, task_priority))
            self.conn.commit()
        except ValueError:
            return

    def find_tasks(self, task_name):
        """Find the specific task name already exists in the DB
        return 0 if not found, return list of id if it returns"""
        self.db_cursor.execute('SELECT id FROM tasks WHERE name LIKE ?', (task_name + "%", ))
        rows = self.db_cursor.fetchall()
        if rows is None or len(rows) == 0:
            print("No task {0} was found".format(task_name))
            return None
        return rows

    def list_tasks(self):
        """Lists all the available tasks inserted into the db"""
        for row in self.db_cursor.execute('SELECT id, name, priority FROM tasks'):
            print(*row, sep="|")

    def delete_task(self, task_name):
        """Delete the given task from DB"""
        tasks = self.find_tasks(task_name)
        if not tasks:
            print("No tasks found as {0} to delete".format(task_name))
            return
        self.db_cursor.execute('DELETE FROM tasks WHERE name = ?', (task_name,))
        self.conn.commit()

    def update_priority(self, task_name, new_priority):
        """Update priority of a given task name with new priority"""
        tasks = self.find_tasks(task_name)
        if not tasks:
            print("No tasks found as {0} to delete".format(task_name))
            return
        self.db_cursor.execute("UPDATE tasks SET priority = ? WHERE name = ?", \
                                   (new_priority, task_name))
        self.conn.commit()


if __name__ == "__main__":
    try:
        TODO_OBJ = TODO()
        while True:
            print("==========================", \
                  "1. Show Tasks", \
                  "2. Add Task", \
                  "3. Change Priority", \
                  "4. Delete Task", \
                  "5. Find Task", \
                  "6. Exit",
                  "==========================", sep='\n')
            USER_OPTION = int(input("Please enter your option: "))

            if USER_OPTION == 1:
                TODO_OBJ.list_tasks()
            elif USER_OPTION == 2:
                NAME = input("Enter a task name: ")
                PRIORITY = int(input("Enter task priority: "))
                TODO_OBJ.add_task(task_name=NAME, task_priority=PRIORITY)
            elif USER_OPTION == 3:
                NAME = input("Enter a task name to update priority: ")
                PRIORITY = int(input("Enter new task priority to be updated: "))
                TODO_OBJ.update_priority(task_name=NAME, new_priority=PRIORITY)
            elif USER_OPTION == 4:
                NAME = input("Enter a task name to delete: ")
                TODO_OBJ.delete_task(task_name=NAME)
            elif USER_OPTION == 5:
                NAME = input("Enter a task name to find: ")
                if TODO_OBJ.find_tasks(NAME):
                    print("***Given task was found in the list***")
            elif USER_OPTION == 6:
                print("Thanks for using our tool, quitting...")
                break
            else:
                print("Unknow option was selected, plesae use correct choice")

    except ValueError as err:
        print("ValueError {0}".format(err))
    except Exception as ex: #pylint: disable=broad-except
        print("{0}".format(ex))
    else:
        print("All completed successfully")
