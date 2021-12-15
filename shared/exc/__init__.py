class BaseError(Exception):
    def __init__(self, *args) -> None:
        self.message = args[0] if args else None

    def __str__(self) -> str:
        return self.message if self.message else ""
