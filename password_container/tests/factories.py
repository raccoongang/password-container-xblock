from factory import DjangoModelFactory

from password_container.models import UserExamSession

class ExamSessionFactory(DjangoModelFactory):
    FACTORY_FOR = UserExamSession
