

class DuplicateDataError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_data = args[0]