import datetime
from mock import Mock

from django.utils import timezone

from student.tests.factories import UserFactory
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

from factories import ExamSessionFactory
from password_container import MAX_TRIES

class PasswordContainerXBlockTests(ModuleStoreTestCase):
    def setUp(self):
        super(PasswordContainerXBlockTests, self).setUp(create_user=False)
        self.course = CourseFactory()
        self.user = UserFactory()
        self.pc = ItemFactory(parent=self.course, category="password_container")
        self.pc.xmodule_runtime = Mock()
        self.pc.xmodule_runtime.user_id = self.user.id
        self.pc.session_id = "exam1"

    def test_user_with_exam_session_already_started_and_has_time(self):
        exam_session = ExamSessionFactory(id=self.pc.session_id,
                                          course_id=self.course.id,
                                          user=self.user,
                                          start_time=timezone.now())
        self.pc.exam_session_duration = 30
        self.pc.display_children_content = Mock()
        frag = self.pc.student_view()
        self.pc.display_children_content.assert_called()

    def test_user_with_exam_session_already_started_and_has_no_time(self):
        exam_session = ExamSessionFactory(id=self.pc.session_id,
                                          course_id=self.course.id,
                                          user=self.user,
                                          start_time=timezone.now() - datetime.timedelta(minutes=10))
        self.pc.exam_session_duration = 5
        self.pc.time_elapsed = Mock()
        frag = self.pc.student_view()
        self.pc.time_elapsed.assert_called()

    def test_user_with_not_started_session(self):
        exam_session = ExamSessionFactory(id=self.pc.session_id,
                                          course_id=self.course.id,
                                          user=self.user)
        self.pc.ask_password = Mock()
        frag = self.pc.student_view()
        self.pc.ask_password.assert_called()

    def test_user_with_not_started_session_and_all_password_attempts_failed(self):
        exam_session = ExamSessionFactory(id=self.pc.session_id,
                                          course_id=self.course.id,
                                          user=self.user,
                                          password_attempts=MAX_TRIES + 1)
        frag = self.pc.student_view()
        






