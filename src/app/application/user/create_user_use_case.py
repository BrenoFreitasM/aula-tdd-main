from uuid import UUID, uuid4
from domain.user.user_repository_interface import UserRepositoryInterface
from dataclasses import dataclass
from domain.user.user_entity import User

# INPUT
@dataclass
class CreateUserRequest:
    name: str

# OUTPUT
@dataclass
class CreateUserResponse:
    id: UUID
    name: str


class CreateUserUseCase:

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        user = User(id=uuid4(), name=request.name)
        self.repository.save(user)
        return CreateUserResponse(id=user.id, name=user.name)