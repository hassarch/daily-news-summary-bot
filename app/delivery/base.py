class BaseSender:
    def send(self, content: str):
        raise NotImplementedError("Sender must implement send()")
