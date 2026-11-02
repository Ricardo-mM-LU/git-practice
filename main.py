def allocate_task(agent,task):
	return{
		"agent":agent,
		"task":task
}
result = allocate_task("robot_1","task_1")
print(result)