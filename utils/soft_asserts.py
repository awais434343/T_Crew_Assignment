class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, message=None):
        try:
            assert actual == expected, message or f"Expected {expected} but got {actual}"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_not_equal(self, actual, expected, message=None):
        try:
            assert actual != expected, message or f"Expected {expected} to not equal {actual}"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_pass(self, condition, message=None):
        try:
            assert condition, message or "Expected condition to pass but it failed"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_fail(self, condition, message=None):
        try:
            assert not condition, message or "Expected condition to fail but it passed"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_true(self, condition, message=None):
        try:
            assert condition, message or "Condition was not True"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_false(self, condition, message=None):
        try:
            assert not condition, message or "Condition was not False"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_in(self, member, container, message=None):
        try:
            assert member in container, message or f"{member} not found in {container}"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_not_in(self, member, container, message=None):
        try:
            assert member not in container, message or f"{member} unexpectedly found in {container}"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_is_none(self, obj, message=None):
        try:
            assert obj is None, message or f"Expected None but got {obj}"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_is_not_none(self, obj, message=None):
        try:
            assert obj is not None, message or "Expected not None but got None"
            return True
        except AssertionError as e:
            self.errors.append(str(e))
            return False

    def assert_raises(self, expected_exception, callable_obj, *args, **kwargs):
        try:
            callable_obj(*args, **kwargs)
            self.errors.append(f"Expected {expected_exception} to be raised, but no exception was raised")
            return False
        except expected_exception:
            return True  # Expected exception was raised

    def assert_not_raises(self, unexpected_exception, callable_obj, *args, **kwargs):
        try:
            callable_obj(*args, **kwargs)
            return True
        except unexpected_exception as e:
            self.errors.append(f"Unexpected exception {type(e).__name__} was raised: {e}")
            return False

    def assert_all(self):
        """Raise an AssertionError if any soft assertion has failed."""
        if self.errors:
            failure_messages = "\n".join(self.errors)
            self.errors.clear()
            raise AssertionError(f"Soft Assertions Failed:\n{failure_messages}")
