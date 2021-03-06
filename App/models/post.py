from orator import Model
from orator.orm import has_many

from App.Database.db import Model

class Post(Model):

    @has_many
    def comments(self):
        from .comment import Comment

        return Comment
