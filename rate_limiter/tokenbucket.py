import time

class TokenBucketRateLimiter():
    """
    Each request uses 1 token. Once all tokens are depleted, wait until bucket refills.
    """

    def __init__(self, tokens_max: int, refill_rate: int):
        self.tokens_max = tokens_max
        self.refill_rate = refill_rate