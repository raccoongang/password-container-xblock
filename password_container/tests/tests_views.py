from mock import Mock

from django.utils import timezone

from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory




class PasswordContainerXBlockTests(ModuleStoreTestCase):
    def setUp(self):
        super(PasswordContainerXBlockTests, self).setUp(create_user=False)
        self.course = CourseFactory()
        self.pc = ItemFactory(parent=self.course, category="password_container")


    def test_user_allowed(self):
        self.pc.get_configuration("group1")
        self.pc.set_user_allowed(True)
        self.pc.set_user_start_time(timezone.now())
        self.pc.configuration.duration = 30
        self.pc.display_children_content = Mock()
        frag = self.pc.student_view()
        self.pc.display_children_content.assert_called()

