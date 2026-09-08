from rate_limiter.tokenbucket import TokenBucketRateLimiter
from random import randint

class RateLimiter():

    def __init__(self):
        randomnumber = str(randint(1,1000000000))
        self._id = str("ID",randomnumber)
        self.bucket = TokenBucketRateLimiter(5,1)

    def allow(self, id: str, bucket: TokenBucketRateLimiter) -> bool:
        return bucket.tokencheck(id)