#Task Browser


This project assumes each task & subtask can be classified as a task.

Most of logic for the project exists in "app" and "task_api" apps. Please note, logic for task status resides in "app/task_api/task_helper" and logic for populating database with data is at "app/db_load.py"

The app developed was containerised using Docker, and exposes an endpoint to view tasks at [/api/tasks](http://127.0.0.1:8000/api/tasks/).

The reoccuring theme found in this task, was recursion. Whereby it was necessary to reverse patterns (e.g. list of parent task nodes) and undertake a bottoms up approach to development such that parent node statuses could be obtained.

Ideally, one would develop an authentication capability which contains task owner's name, and there was an ommission of attempts to include this and priority (as well as overriding the get_queryset method to list each task and its children in hierarchical order). Further to be added, would be a chronjob, where the status of the application would need to be refreshed every x mins due to leaf nodes depending on current time.

## Installation
```
docker-compose up --build
```






