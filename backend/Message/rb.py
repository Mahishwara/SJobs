class RBMessage:
    def __init__(self, id: int | None = None,
                 id_to: str | None = None,
                 id_from: str | None = None):
        self.id = id
        self.id_to = id_to
        self.id_from = id_from


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'id_to': self.id_to,
                'id_from': self.id_from}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data