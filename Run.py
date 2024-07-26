from logs.HRLogging import HRLogging
import os


#test
log = HRLogging()
log.push_log_critical("2")

name = os.environ.get("REDIS_USER")
password = os.environ.get("REDIS_USER_PASSWORD")

print(name,password)

if __name__=="__main__":
    pass