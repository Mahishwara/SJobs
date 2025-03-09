class RBFeedback:
    def __init__(self, id: int | None = None,
                 id_student: str | None = None,
                 id_employer: str | None = None):
        self.id = id
        self.id_student = id_student
        self.id_employer = id_employer


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'id_student': self.id_student,
                'id_employer': self.id_employer}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data