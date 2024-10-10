from ..environment import env


REDIS_URL = env.str("BE_SKELETON_TEST_REDIS_URL", default="redis://redis:6379/2")
