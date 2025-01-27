from abc import ABC, abstractmethod
from domain.user.user_entity import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def save(self, user:User) -> None:
        raise NotImplementedError