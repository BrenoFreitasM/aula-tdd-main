from unittest.mock import MagicMock
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse

class TestCreateUser:

    # TESTE PARA CRIAR UM USUÁRIO COM DADOS VÁLIDOS
    def test_create_user_with_valid_data(self):

        # REPOSITORIO
        mock_repository = MagicMock(UserRepositoryInterface)

        # CASO DE USO
        use_case = CreateUserUseCase(repository=mock_repository)

        # INPUT (REQUEST)
        request = CreateUserRequest(name="Alexandre")

        # OUTPUT (RESPONSE)
        response = use_case.execute(request)

        assert response.id is not None 
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True
