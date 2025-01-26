from domain.user.user_entity import User
from domain.task.task_entity import Task
from uuid import uuid4

class TestUserWithTasks:

    # TESTE PARA ADICIONAR TAREFAS AO USUÁRIO
    def test_collect_tasks(self):

        user = User(id=uuid4(), name="Willian Salvador da Pátria")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testess de integração",
            description="Descrição 1",
            completed=False
        )

        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes unitários",
            description="Descrição 2",
            completed=False
        )

        user.collect_tasks([task1, task2])

        assert len(user.tasks) == 2 
        assert task1 in user.tasks
        assert task2 in user.tasks