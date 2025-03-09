class RBStudent:
    def __init__(self, id: int | None = None,
                 firstname: str | None = None,
                 lastname: str | None = None,
                 post: str | None = None,
                 level_skill: int | None = None,
                 speciality: str | None = None,
                 course: int | None = None,
                 ability: str | None = None,
                 ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.post = post
        self.level_skill = level_skill
        self.speciality = speciality
        self.course = course
        self.ability = ability


    def to_dict(self) -> dict:
        data = {'id': self.id,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'post': self.post,
                'level_skill': self.level_skill,
                'speciality': self.speciality,
                'course': self.course,
                'ability': self.ability}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data