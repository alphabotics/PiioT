from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('uuid')
            table.string('email')
            table.text('password')
            table.string('first_name')
            table.string('last_name')
            table.string('phone', 11)
            table.string('job_title')
            table.enum('gender', ['male', 'female'])
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
