from environs import Env

env = Env()
env.read_env()

OTP_LOWER_LIMIT = env.int("OTP_LOWER_LIMIT", default=1111)
OTP_UPPER_LIMIT = env.int("OTP_UPPER_LIMIT", default=9999)
