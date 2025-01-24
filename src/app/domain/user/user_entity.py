from uuid import UUID, uuid4

class User:

    id: UUID
    name: str

    def __init__(self, id:UUID, name:str ):
        self.id = id
        self.name = name
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("Id must be an UUID")

# user = User(id=uuid4(), name="Maria")

# print(user.id)
# print(user.name)