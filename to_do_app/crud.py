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
def delete(task_id:int):
    tasks=load_data()

    for task in tasks:
        if task['id']==task_id:
            tasks.remove(task)
            with open('data.json', 'w') as file:
                json.dump(task, file)
            
            return {'message:task deleted'}
        else:
            return{'error:task is not available'}
        


#update the task
def update(task_id,update_task):
    task=load_data()

    for t in task:
        if t['id']==task_id:
            t['title']=update_task['title']
            t['description']=update_task['description']

            with open('data.json','w') as file:
                json.dump(task,file)

            return {'message':'task updated successfylly'}
        
        else:
            return{'error':'task is not present'}
        


#to create new task

def create(new):
    tasks=load_data()
    new={
        'id':len(tasks)+1,
        'title':new.title,
        'description':new.description
    }
    tasks.append(new)
    with open('data.json','w') as file:
        json.dump(new,file)
    return {'message':'new task added '}

    