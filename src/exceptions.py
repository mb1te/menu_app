class NotFound(Exception):
    def __init__(self, entity: str) -> None:
        super().__init__()
        self.entity = entity
