# Aula 01:56:52
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

class TestGetUserById:

    # TESTAR SE É POSSÍVEL RETORNAR UM USUÁRIO PELO ID DELE
    def test_can_get_user_by_id(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        # retornar o usuário 1 pelo seu id
        user = repository.get_by_id(user1.id)

        # verifico se eu retorno o mesmo usuário
        assert user.id == user1.id
        assert user.name == user1.name
    
    # TESTAR SE O METÓDO get_by_id  RETORNA UMA OBJETO VAZIO CASO NÃO EXISTA O USUÁRIO NO REPOSITÓRIO
    def test_when_user_does_not_exist_should_return_none(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user_id=uuid4())

        assert user == None

class TestUpdateUser:

    # TESTAR SE É POSSÍVEL ATUALIZAR O NOME DE UM USUÁRIO
    def test_update_user(self):
        repository = InMemoryUserRepository()
        user1 = User(id=uuid4(), name="João")
        user2 = User(id=uuid4(), name="Emidio")

        repository.save(user1)
        repository.save(user2)

        # atualizando o nome do usuário João
        user1.name = "Matheus"
        repository.update(user1)

        updated_user = repository.get_by_id(user_id=user1.id)

        assert updated_user.name == "Matheus"
