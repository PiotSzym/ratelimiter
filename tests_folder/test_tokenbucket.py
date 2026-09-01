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

def test_token_max(testbucket):
    for i in range(3):
        assert testbucket.tokencheck("testID") is True, f"Token check failed at iteration {i+1}"

def test_token_caps_at_max(testbucket, monkeypatch):
    testbucket.tokencheck("testID")
    real_time = time.time
    monkeypatch.setattr(time, "time", lambda: real_time() + 1000)

    assert testbucket.tokencheck("testID") is True
    assert testbucket.tokencheck("testID") is True
    assert testbucket.tokencheck("testID") is True
    assert testbucket.tokencheck("testID") is False

def test_tokens_refill_over_time(testbucket, monkeypatch):
    for i in range(3):
        testbucket.tokencheck("testID")
    assert testbucket.tokencheck("testID") is False

    real_time = time.time
    monkeypatch.setattr(time, "time", lambda: real_time() + 1)
    assert testbucket.tokencheck("testID") is True

def test_different_keys_independent(testbucket):
    for i in range(3):
        testbucket.tokencheck("testID")
        
    assert testbucket.tokencheck("testID") is False
    assert testbucket.tokencheck("testID2") is True