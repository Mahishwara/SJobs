class RBStudent:
    def __init__(self, id: int | None = None,
                 firstname: str | None = None,
                 lastname: str | None = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'firstname': self.firstname,
                'lastname': self.lastname}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data