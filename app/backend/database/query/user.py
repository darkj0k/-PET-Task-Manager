user_table_create = '''
DROP TABLE IF EXISTS tasks ;
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    vip BOOLEAN DEFAULT FALSE
);
'''