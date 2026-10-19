import time

class TokenBucketRateLimiter():
    # Each request uses 1 token. Once all tokens are depleted, wait until bucket refills.

    def __init__(self, tokens_max: int, refill_rate: float) -> None:
        '''
        time to refill is 1/refill_rate
        The underscore is used to encapsulate buckets for each user
        '''
        self.tokens_max = tokens_max
        self.refill_rate = refill_rate
        self._buckets = {}
        

    def bucket(self, id: str) -> dict:
        timenow = time.time()

        if id not in self._buckets:

            self._buckets[id] = {
                "tokens": self.tokens_max,
                "max": self.tokens_max,
                "refill": self.refill_rate,
                "latest_refill": timenow
            }
        return self._buckets[id]
    
    def refill(self, bucket: dict) -> None:
        timenow = time.time()
        elapsed = timenow - bucket["latest_refill"]
        bucket["tokens"] = min(bucket["max"], bucket["tokens"] + elapsed * bucket["refill"])
        bucket["latest_refill"] = timenow
    
    def changemax(self, id: str, delta_max: int) -> None:
        bucket = self.bucket(id)
        self.refill(bucket)
        bucket["max"] = max(1, bucket["max"] + delta_max)
        bucket["tokens"] = min(bucket["tokens"], bucket["max"])

    def changerefill(self, id: str, delta_refill: float) -> None:
        bucket = self.bucket(id)
        self.refill(bucket)
        bucket["refill"] = max(0.1, bucket["refill"] + delta_refill)

    def tokencheck(self, id: str) -> bool:
        bucket = self.bucket(id)
        self.refill(bucket)
        if bucket["tokens"] < 1:
            return False
        bucket["tokens"] -= 1
        return True