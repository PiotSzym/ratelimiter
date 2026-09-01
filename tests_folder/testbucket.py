import pytest
from rate_limiter.tokenbucket import TokenBucketRateLimiter

@pytest.fixture
def limiter():
    limit = TokenBucketRateLimiter()
    return limit