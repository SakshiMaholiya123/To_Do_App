from fastapi import APIRouter
from schemas import Task,User
from crud import (create, get_tasks,get_specific_task,delete, update)
from auth import create_token

router=APIRouter()

#route to get all tasks
@router.get('/tasks')
def all_tasks():
    return get_tasks()

#route to get the specific task using id
@router.get('/tasks/{task_id}')
def get_a_task(task_id:int):
    return get_specific_task(task_id)


#route to delete a task

@router.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    return delete(task_id)


#route to update a task
@router.put('/tasks/{task_id}')
def update_task(task_id:int,task:Task):
    return update(task_id,task)


#route to add the new task
@router.post('/tasks')
def add_task(task: Task):
    return create(task)


#route for login
@router.post("/login")
def login(user:User):

    #username validation
    if user.name.strip() == "":
        return {
            "error":"username cant empty"
        }

    # password validation
    if user.password.strip() == "":
        return {
            "error": "password cant empty"
        }

    # password length validation
    if len(user.password) < 6:
        return {
            "error": "password must be of atleast 6 characters"
        }

    # demo authentication
    if user.name!="admin":
        return {
            "error": "invalid username"
        }

    if user.password!="admin123":
        return {
            "error": "invalid password"
        }

    # create jwt token
    token=create_token(
        data={"sub":user.name}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }