# AULA TDD | 02:40:40
from uuid import uuid4
from domain.task.task_entity import Task
import pytest

class TestTask:

    # TESTE PARA VERIFICAR O CONSTRUTOR DA CLASSE TAREFA
    def test_task_initialization(self):

        task_id = uuid4()
        user_id = uuid4()
        title = "Estudar mais sobre testes unitários."
        description = "Os testes unitários são os mais baratos."
        completed = False

        task = Task(
            id=task_id,
            user_id=user_id,
            title=title,
            description=description,
            completed=completed
        )

        assert task.id == task_id
        assert task.user_id == user_id
        assert task.title ==  title
        assert task.description ==  description
        assert task.completed ==  completed

    # TEST PARA VALIDAÇÃO A VALIDAÇÃO DO ID DA TAREFA
    def test_task_id_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="id must be an UUID"):
            Task(
                id=1,
                user_id=user_id,
                title="Título tarefa",
                description="Descrição tarefa",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DO ID DO USUÁRIO VALIDO
    def test_task_user_id_validation(self):
        task_id = uuid4()
        with pytest.raises(Exception, match="user_id must be aan UUID"):
            Task(
                id=task_id,
                user_id="Invalid_user_id",
                title="Título da tarefa",
                description="Descrição tarefa",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DO TÍTULO DA TAREFA
    def test_task_title_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="title is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="",
                description="Descrição tarefa",
                completed=False
            )


    # TESTE PARA VERIFICAR A VALIDAÇÃO TÍTULO DA DESCRIÇÃO
    def test_task_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="description is required"):
            Task(
                id=task_id,
                user_id=user_id,
                title="Título da tarefa",
                description="",
                completed=False
            )

    # TESTE PARA VERIFICAR A VALIDAÇÃO DO STATUS "COMPLETED" DA TAREFA
    def test_task_description_validation(self):
        task_id = uuid4()
        user_id = uuid4()
        with pytest.raises(Exception, match="invalid complered status: must be a boolean"):
            Task(
                id=task_id,
                user_id=user_id,
                title="Título da tarefa",
                description="Descrição da tarefa",
                completed="not_boolean"
            )
        
    # TESTE PARA VERIFICAR SE UMA TAREFA FOI COMPLETADA COM UMA FUNÇÃO mark_as_completed
    def test_mark_as_completed(self):
        # instanciar a minha classe Task
        task = Task(
            id=uuid4(),
            user_id=uuid4(),
            title="Título da tarefa",
            description="Descrição da tarefa",
            completed=False
        )

        # marcar a tarefa como clioncluída
        task.mark_as_completed()

        # verificar se o atrivuto foi atualizado para completed
        assert task.completed == True