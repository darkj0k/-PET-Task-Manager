from app.backend.schemas import Task


task_table_create = '''
DROP TABLE IF EXISTS tasks;
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
'''
task_get_all = lambda id: f'''
SELECT title, description FROM tasks WHERE user_id = {id} ORDER BY tasks.priority
'''

def task_add(task_data: dict, user_id: int):
    fields = ", ".join(task_data.keys()) 
    values = ", ".join(repr(value) for value in task_data.values())  

    fields += ", user_id"
    values += f", {user_id}"
    query = f'''
    INSERT INTO tasks ({fields}) VALUES ({values})
    '''
    print(repr(query))
    return query


def task_update(task_data: dict, task_id: int):
    attributes = []
    for key, value in task_data.items():
        query = '%s = "%s"' % (key, value)
        attributes.append(query)
    varible = ",".join(attributes)
    query = f'''
    UPDATE tasks SET {varible} WHERE id = {task_id}
    '''
    return query


task_delete = lambda task_id: f'''
    DELETE FROM tasks WHERE id = {task_id}
'''