from domain.user.user_repository_interface import UserRepositoryInterface
from domain.user.user_entity import User

class InMemoryUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []

    def save(self, user: User) -> None:
        self.users.append(user)