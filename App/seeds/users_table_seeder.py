from orator.seeds import Seeder
from orator.orm import Factory
from App.models.user import User
from App.models.post import Post
from .seed_helper import random_with_N_digits
import uuid
import random

factory = Factory()


@factory.define(User)
def users_factory(faker):
    return {
        'uuid': faker.uuid4(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'password': faker.password(),
        'phone': random_with_N_digits(11),
        'job_title': faker.job(),
    }


@factory.define(Post)
def posts_factory(faker):
    return {
        'title': faker.name(),
        'content': faker.text()
    }


class UsersTableSeeder(Seeder):

    factory = factory  # This is only needed when using an external factory

    def run(self):
        """
        Run the database seeds.
        """
        self.factory(User, 50).create().each(
            lambda u: u.posts().save(self.factory(Post).make())
        )