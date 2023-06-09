import uuid

import redis
from random import randint


class RedisClient(redis.Redis):
    def create_user_registration_code(self, email):
        code = str(uuid.uuid4())
        self.set(email, code)
        self.expire(email, 900)
        return code

    def check_user_registration_code(self, email, activation_key):
        return (
            False
            if not self.exists(email) or self.get(email) != activation_key
            else True
        )


RedisDB = RedisClient(host="localhost", port=6379, decode_responses=True)
