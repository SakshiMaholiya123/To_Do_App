from fastapi import APIRouter
from schemas import Task
from crud import (get_tasks,get_specific_task,delete)

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
def delete_task(task_id):
    return delete(task_id)
