from orator.orm import has_many

from App.Database.db import Model


class User(Model):

    __hidden__ = ['password']

    @has_many
    def posts(self):
        from .post import Post

        return Post

    @has_many
    def comments(self):
        from .comment import Comments

        return Comments