from django.db import models
# auth_user model import. It already exists since it's Djando native
from  django.contrib.auth.models import User

# Create "barks" table model
class Bark(models.Model):
    # id column is created by default
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Called "user" because Django rename it as user_id after
    content = models.CharField(max_length=140) # CharField to add 140 limit constrain
    created_at = models.DateTimeField(auto_now_add=True) # To set the first time bark creation only

    # method to show the content on the admin panel.
    # It takes the username from user and limit the content to 20 chars
    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
