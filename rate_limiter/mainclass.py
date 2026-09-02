from tokenbucket import TokenBucketRateLimiter
from random import randint

class RateLimiter():

    def __init__(self):
        self.__id = str("ID",randint(1,1000000000))
        self.bucket = TokenBucketRateLimiter(5,1)

    """
    __ makes the id private so that it cant be changed by the user
    """

    def allow(self, id: str, bucket: TokenBucketRateLimiter) -> bool:
        return bucket.tokencheck(id)