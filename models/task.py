from db.database import DB


def addTask(title, complete, description = None, due_date = None):
    with DB() as cursor:
        cursor.execute('''
            INSERT INTO tasks (title, description, due_date, completed)
            VALUES (?, ?, ?, ?)
        ''', (title, description, due_date, complete)) 

def updateTask(task_id, title, complete, description = None, due_date = None):
    with DB() as cursor:
        cursor.execute('''
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?, completed = ?
            WHERE id = ?
        ''', (title, description, due_date, complete, task_id))

def deleteTask(task_id):
    with DB() as cursor:
        cursor.execute('''
            DELETE FROM tasks
            WHERE id = ?
        ''', (task_id,))
        
def completeTask(task_id):
    with DB() as cursor:
        cursor.execute('''
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
        ''', (task_id,))

def unccmpleteTask(task_id):
    with DB() as cursor:
        cursor.execute('''
            UPDATE tasks
            SET completed = 0
            WHERE id = ?
        ''', (task_id,))
        
def deleteAllTasks():
    with DB() as cursor:
        cursor.execute('''
            DELETE FROM tasks
        ''')
        
def completeAllTasks():
    with DB() as cursor:
        cursor.execute('''
            UPDATE tasks
            SET completed = 1
        ''')
        
def uncompleteAllTasks():
    with DB() as cursor:
        cursor.execute('''
            UPDATE tasks
            SET completed = 0
        ''')
        
def deleteCompletedTasks():
    with DB() as cursor:
        cursor.execute('''
            DELETE FROM tasks
            WHERE completed = 1
        ''')

def getTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
        ''')
        return cursor.fetchall()
    
def getTask(task_id):
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks WHERE id = ?
        ''', (task_id,))
        return cursor.fetchone()
    
def getTaskByTitle(title):
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE title LIKE ?
        ''', (f"%{title}%",))
        return cursor.fetchall()
    
def getCompletedTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE completed = 1
        ''')
        return cursor.fetchall()
    
def getUncompletedTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE completed = 0
        ''')
        return cursor.fetchall()
    
def getOverdueTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date < datetime('now') AND completed = 0
        ''')
        return cursor.fetchall()
    
def getDueTodayTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date >= date('now') AND due_date < date('now', '+1 day') AND completed = 0
        ''')
        return cursor.fetchall()
    
def getDueThisWeekTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date >= date('now') AND due_date < date('now', '+7 day') AND completed = 0
        ''')
        return cursor.fetchall()
    
def getDueThisMonthTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date >= date('now') AND due_date < date('now', '+1 month') AND completed = 0
        ''')
        return cursor.fetchall()

def getFutureTasks():
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date >= date('now') AND completed = 0
        ''')
        return cursor.fetchall()

def getByDescription(description):
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE description LIKE ?
        ''', (f"%{description}%",))
        return cursor.fetchall()
        
        
def getByDueDate(due_date):
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date = ?
        ''', (due_date,))
        return cursor.fetchall()
    
def getByDueDateRange(start_date, end_date):
    with DB() as cursor:
        cursor.execute('''
            SELECT * FROM tasks
            WHERE due_date >= ? AND due_date <= ?
        ''', (start_date, end_date))
        return cursor.fetchall()
    
