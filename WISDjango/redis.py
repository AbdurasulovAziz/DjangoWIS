import redis
from random import randint


class Redis(redis.Redis):

    def create_user_registration_code(self, email):
        code = randint(10000, 99999)
        self.set(email, code)
        self.expire(email, 600)
        return code

    def check_user_registration_code(self, email, code):
        if not self.get(email):
            return "Ваш код истек или не существует. Попробуйте пройти повторную регистрацию"

        if self.get(email) != code:
            return "Код невереный"

        return True


RedisDB = Redis(host='localhost', port=6379, decode_responses=True)

