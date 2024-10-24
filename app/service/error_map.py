class ErrorMap:
    """
    This class provides a mapping between exceptions and error messages.
    """

    def __init__(self):
        self._error_map = {}

    def add_error(self, field, error_message):
        self._error_map[field] = error_message
        return self

    def get_error(self, field):
        return self._error_map.get(field, None)

    def get_errors(self):
        return self._error_map

    def has_errors(self):
        return len(self._error_map) > 0
