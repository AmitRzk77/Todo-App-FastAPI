from celery import Celery


celery = Celery(
    "todo_tasks",
    broker="redis://localhost:6379/0",  
    backend="redis://localhost:6379/0"
)

@celery.task
def notify_task_created(task_id, title):
    
    print(f"✅ Background Task: New ToDo Created - ID: {task_id}, Title: '{title}'")
    return f"Notification sent for task {task_id}"
