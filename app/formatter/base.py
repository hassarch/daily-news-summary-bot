class BaseFormatter:
    def format(self, data: dict) -> str:
        raise NotImplementedError("Formatter must implement format()")
