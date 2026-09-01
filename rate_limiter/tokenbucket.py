import time

class TokenBucketRateLimiter():
    """
    Each request uses 1 token. Once all tokens are depleted, wait until bucket refills.
    """

    def __init__(self, tokens_max: int, refill_rate: float) -> None:
        """
        time to refill is 1/refill_rate
        The underscore is used to encapsulate buckets for each user
        """
        self.tokens_max = tokens_max
        self.refill_rate = refill_rate
        self._buckets = {}
        

    def tokencheck(self, id:str) -> bool:
        """
        Init bucket for user if there isnt one already
        Refill the bucket if enough time has passed
        Check if the bucket has enough tokens
        Return bool whether token was used or not enough tokens available
        """

        timenow = time.time()

        if id not in self._buckets:
            self._buckets[id] = {
                "tokens": self.tokens_max,
                "latest_refill": timenow
            }

        bucket = self._buckets[id]

        time_since_last_refill = timenow - bucket["latest_refill"]

        tokens_now = min(self.tokens_max, bucket["tokens"] + time_since_last_refill*self.refill_rate)

        bucket["tokens"] = tokens_now

        bucket["latest_refill"] = timenow

        if bucket["tokens"] < 1:
            return False

        bucket["tokens"] -= 1
        return True