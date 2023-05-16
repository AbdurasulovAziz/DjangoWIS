import uuid

import redis
from random import randint


class Redis(redis.Redis):

    def create_user_registration_code(self, email):
        code = str(uuid.uuid4())
        self.set(email, code)
        self.expire(email, 900)
        return code

    def check_user_registration_code(self, email, activation_key):
        if not self.exists(email) or self.get(email) != activation_key:
            return False

        return True


RedisDB = Redis(host='localhost', port=6379, decode_responses=True)

