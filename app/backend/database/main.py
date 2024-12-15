from asyncpg import connect
from app.backend.settings.settings import env_settings
from app.backend.database.query.task import task_table_create
from app.backend.database.query.user import user_table_create
class DataBasePool:
    async def create_pool(self):
        self.conn = await connect(self.URL)
        self.transaction = self.conn.transaction()
    async def migration(self):
        async with self.transaction:
            await self.conn.execute(user_table_create)
            await self.conn.execute(task_table_create)
    

    async def close(self):
        await self.conn.close()

    async def operation(self, query, type, *args):
        async with self.transaction:
            exec = await self.conn.execute(query(*args))
            if type.lower() == "select":
                result = await exec.fetchall()
                return result
            return None
    
    async def __aenter__(self):
        await self.create_pool()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    


pool = DataBasePool()
