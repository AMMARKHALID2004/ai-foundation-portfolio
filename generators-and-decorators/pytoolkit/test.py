import timer
import logging_deco
import retry
import caching
import rate_limit
import time

def test_timer():
    @timer.timer
    def sample_func(x):
        return x * 2
    
    # Assert the wrapped function's return value is still correct
    assert sample_func(5) == 10


def test_logger():
    @logging_deco.logger
    def sample_func(x, y):
        return x + y
    
    # Assert the return value remains unchanged after wrapping
    assert sample_func(10, 20) == 30


def test_memoize():
    execution_state = {"count": 0}  # Tracks execution local to this test

    @caching.memoize
    def expensive_func(x):
        execution_state["count"] += 1
        return x * 10

    # First call: computes and returns
    res1 = expensive_func(4)
    # Second call: fetches from cache
    res2 = expensive_func(4)

    # Assert that calling twice returns the identical correct result
    assert res1 == 40
    assert res2 == 40
    # Assert the underlying function only actually executed once
    assert execution_state["count"] == 1


def test_retry():
    # ---- Scenario A: Fails twice, then succeeds on the 3rd attempt ----
    state_a = {"attempts": 0}

    @retry.retry(3)
    def flaky_func():
        state_a["attempts"] += 1
        if state_a["attempts"] < 3:
            raise ValueError("Temporary failure")
        return "success"

    # Assert it eventually returns the success value when wrapped with @retry(3)
    assert flaky_func() == "success"

    # ---- Scenario B: Always fails, wrapped with @retry(2) ----
    @retry.retry(2)
    def failing_func():
        raise RuntimeError("Permanent failure")

    # Use try/except + assert False to verify exception gets properly raised
    try:
        failing_func()
        assert False, "Exception was not raised despite exceeding retry limits"
    except RuntimeError:
        pass  # Successfully caught the exception, test passes


def test_rate_limit():
    @rate_limit.rate_limit(1)  # 1-second limit
    def target_func():
        return "Allowed"

    # Assert the first call succeeds
    assert target_func() == "Allowed"
    
    # Assert that an immediate second call is blocked
    assert target_func() is None



# Run all tests when file is executed directly
if __name__ == "__main__":
    test_timer()
    test_logger()
    test_memoize()
    test_retry()
    test_rate_limit()
    print("All tests passed successfully!")