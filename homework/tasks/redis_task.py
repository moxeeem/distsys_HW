import redis.asyncio as aredis


class UsersByTitleStorage:
    def __init__(self):
        self._client = aredis.StrictRedis()

    async def connect(self) -> None:
        pass

    async def disconnect(self) -> None:
        await self._client.aclose()

    async def save_item(self, user_id: int, title: str) -> None:
        """
        Напишите код для сохранения записей таким образом, чтобы в дальнейшем
        можно было за один запрос получить список уникальных пользователей,
        имеющих объявления с заданным заголовком.
        """
        key = f'title:{title}'
        await self._client.sadd(key, user_id)

    async def find_users_by_title(self, title: str) -> list[int]:
        """
        Напишите код для поиска уникальных user_id, имеющих хотя бы одно объявление
        с заданным title.
        """
        key = f'title:{title}'
        members = await self._client.smembers(key)
        return [int(member) for member in members]
    
