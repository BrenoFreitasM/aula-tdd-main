# Aula 01:34:52
from domain.user.user_entity import User
from uuid import uuid4
from infra.user.in_memory_user_repository import InMemoryUserRepository

class TestSaveUser:

    # TESTAR SE É POSSÍVEL SALVAR USUÁRIO NO REPOSITÓRIO
    def test_can_save_user(self):

        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")


        # salvar o usuário user1 no repositório
        repository.save(user1)
        # salvar o usuário user2 no repositório
        repository.save(user2)
        

        # repository.users = [ User(id=uuid4(), name="João"), User(id=uuid4(), name="Emidio")]

        # verificar se os usuários estão dentro do repositório e se a lista de usuário tem 2 usuários
        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2