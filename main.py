from fastapi import FastAPI
import json

app=FastAPI()

#to reead the json file

def load_data():
    with open('data.json','r') as file:
        data=json.load(file)
    return data


#get the  all tasks

@app.get('/tasks')
def get_tasks():
    task=load_data()
    return task


# delete task
@app.delete(('/tasks/{task_id}'))
def delete(task_id):
    tasks=load_data()

    for task in tasks:
        if task['id']==task_id:
            task.remove(task)
            return {'message:task deleted'}
        else:
            return{'error:task is not available'}