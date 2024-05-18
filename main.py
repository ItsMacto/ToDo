# from db.database import DB
import models.task as Todo 

def main():
    # DB.setup_database()
    print('Welcome to the Ultimate Task Manager \n')
    
    # Todo.addTask('Task 1', False, 'This is the first task', '2024-09-01')
    # Todo.addTask('Task 2', False, 'This is the second task', '2024-09-02')
    
    upcomingTasks = Todo.getUncompletedTasks()()
    if upcomingTasks == []:
        print('No Upcoming Tasks')
    else:
        upcomingTasks.sort(key=lambda x: x[3])
        # after justing getting ID I will check what ones are over due and make
        # them priority
        
        
        
        print('Upcoming tasks:')
            
    # print(Todo.getTasks())
    # Todo.deleteAllTasks()

    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

    
'''
TODO: (lol)
- get should return IDs (I think)

'''