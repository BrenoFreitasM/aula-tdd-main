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

    # TESTE PARA CONTABILIZAR TAREFAS PENDENTES DE UM USUÁRIO
    def test_count_pending_tasks(self):
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

        task3 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes e2e",
            description="Descrição 3",
            completed=False
        )

        user.collect_tasks([task1, task2, task3])
        # marcamos tarefa 1 
        user.tasks[0].mark_as_completed()
        # user.tasks -> 3 tarefas
        # percorrer as tarefas e contar apenas aquelas que estão marcadas como completed == False
        # Deveria retornar 3
        pending_counting = user.count_pending_tasks()
        assert pending_counting == 2
    
    # TESTAR A QUANTIDADE DE TAREFAS PENDENTE QUANDO UM USUÁRIO É CRIADO
    def test_count_peding_task_empty(self):
        user = User(id=uuid4(), name="William")
        count_peding_task = user.count_pending_tasks()
        assert count_peding_task == 0

    # TESTAR QUANDO TODAS AS TAREFAS DO USUÁRIO ESTÃO COMPLETADAS
    def test_all_tasks_completed(self):
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

        # usuário com duas tarefas pendentes
        user.collect_tasks([task1, task2])

        # primeira tarefa da lista marcada como finalizada
        user.tasks[0].mark_as_completed()
        # segunda tarefa da lista marcada como finalizada
        user.tasks[1].mark_as_completed()

        # coletar o retorno da função count_peding_tasks -> deverá retornar 0
        count_peding_tasks = user.count_pending_tasks()

        assert count_peding_tasks == 0

