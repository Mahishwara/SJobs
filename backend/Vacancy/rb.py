class RBVacancy():
    def __init__(self, id: int | None = None,
                 name: str | None = None,
                 description: str | None = None,
                 publication_date: str | None = None,
                 close_date: str | None = None,
                 needed_skill: int | None = None,
                 salary: str | None = None):
        self.id = id
        self.name = name
        self.description = description
        self.publication_date = publication_date
        self.close_date = close_date
        self.needed_skill = needed_skill
        self.salary = salary



    def to_dict(self) -> dict:
        data = {'id': self.id,
                'name': self.name,
                'description': self.description,
                'publication_date': self.publication_date,
                'close_date': self.close_date,
                'needed_skill': self.needed_skill,
                'salary': self.salary}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data