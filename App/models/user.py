import uuid
from orator.orm import has_many
from orator import SoftDeletes

from App.Database.db import Model


class UserObserver(object):

    def creating(self, user):
        user.uuid = str(uuid.uuid4())

    def saving(self, user):
        pass

    def saved(self, user):
        pass

class User(SoftDeletes, Model):

    __dates__ = ['deleted_at']

    __hidden__ = ['password']

    __fillable__ = [
        'email',
        'password',
        'first_name',
        'last_name',
        'job_title',
        'phone'
    ]

    __casts__ = {
        'id': 'int',
        'email': 'str',
        'password': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'job_title': 'str',
        'phone': 'str',
    }

    @has_many
    def posts(self):
        from .post import Post

        return Post

    @has_many
    def comments(self):
        from .comment import Comments

        return Comments


User.observe(UserObserver())