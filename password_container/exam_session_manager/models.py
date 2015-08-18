class ExamSession(models.Model):
    id  = models.CharField(max_length=100, primary_key=True)
    course_id = CourseKeyField(max_length=255, db_index=True)
    duration =  models.IntegerField(default=0)
    password = models.CharField(max_length=100)

    def list_sessions(self, course_id):
        """List all sessions attached to a course"""
        pass
    def reinitialize_all_users_state(self):
        pass
    def reinitialize_user_state(self):
        pass
    def show_user_state(self):
        pass

class ExamSessionUserState(models.Model):
    """Link a user with an exam session."""
    exam_session = models.ForeignKey(ExamSession, db_index=True)
    user = models.ForeignKey(User, db_index=True)

    password_attempts = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)

    class Meta:
        unique_together = (('exam_session', 'user'),)

    def has_started(self):
        return True  if self.start_time else False

