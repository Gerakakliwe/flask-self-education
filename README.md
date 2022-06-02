# flask-self-education
Project for self-educational purposes. No youtube videos are used, only official documentation.

In order to show all tasks:
curl http://localhost:5000/todos

Show one task:
curl http://localhost:5000/todos/todo1

Delete task:
curl http://localhost:5000/todos/todo2 -X DELETE -v

Create new task:
curl http://localhost:5000/todos -H 'Content-type: application/json' -d '{"task":"something new"}' -X POST -v

Update task:
curl http://localhost:5000/todos/todo4 -H 'Content-type: application/json' -d '{"task":"something different"}' -X PUT -v



