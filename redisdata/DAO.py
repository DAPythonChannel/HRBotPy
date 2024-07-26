import redis
from logs.HRLogging import HRLogging

log = HRLogging()
try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    info = r.info()
    print(info['redis_version'])
    response = r.ping()
    if response:
        print("Подключение успешно!")
    else:
        print("Не удалось подключиться к Redis.")
except redis.exceptions.RedisError as e:
    log.push_log_warning(f"Ошибка: {e}")
