from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase

class ExamSessionManagerTest(ModuleStoreTestCase):
    def setUp(self):
        super(ExamSessionManagerTest, self).setUp(create_user=False)
        
