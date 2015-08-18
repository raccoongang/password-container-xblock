from password_container.exam_session_manager.models import ExamSession
from django.forms import ModelForm

class ExamSessionForm(ModelForm):
    class Meta:
        model = ExamSession
        fields = ['duration ', 'password']
    
