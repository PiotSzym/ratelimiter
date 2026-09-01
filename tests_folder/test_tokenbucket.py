import pytest
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rate_limiter.tokenbucket import TokenBucketRateLimiter

starttime = time.time()

@pytest.fixture
def testbucket():
    testbucket = TokenBucketRateLimiter(tokens_max=3, refill_rate=5)
    return testbucket

"""
Each func tests for different cases
"""

def test_tokencheck(testbucket):
    for i in range(3):
        assert testbucket.tokencheck("testID") is True, f"Token check failed at iteration {i+1}"