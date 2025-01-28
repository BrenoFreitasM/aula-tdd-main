from domain.user.user_repository_interface import UserRepositoryInterface
from domain.user.user_entity import User
from uuid import UUID

class InMemoryUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []

    def save(self, user: User) -> None:
        self.users.append(user)

    def get_by_id(self, user_id: UUID) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def update(self, user: User) -> None:
        to_update_user = self.get_by_id(user.id)
        if to_update_user:
            self.users.remove(to_update_user)
            self.users.append(user)