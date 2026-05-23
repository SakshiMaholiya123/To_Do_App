from fastapi import FastAPI
import json

app=FastAPI()

#to read the json file

def load_data():
    with open('data.json','r') as file:
        data=json.load(file)
    return data


#get the  all tasks

def get_tasks():
    task=load_data()
    return task


#to get the specific task
def get_specific_task(task_id:int):
    task=load_data()
    for t in task:
        if t['id']==task_id:
            return t
        else:
            return {"error":"task is not found"}

# delete task
def delete(task_id):
    tasks=load_data()

    for task in tasks:
        if task['id']==task_id:
            task.remove(task)
            return {'message:task deleted'}
        else:
            return{'error:task is not available'}
        


#update the task
