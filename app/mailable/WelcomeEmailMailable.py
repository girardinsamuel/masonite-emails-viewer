"""A WelcomeEmailMailable Mailable."""

from masonite.drivers import Mailable


class WelcomeEmailMailable(Mailable):
    """A WelcomeEmailMailable Mailable."""
    placeholder_variables = {
        'user': 'Samy',
        'account': {
            'email': 'samy@test.fr',
            'first_name': 'Samy'
        }
    }

    def __init__(self, to, variables={}):
        """A WelcomeEmailMailable Initializer."""
        self._to = to
        self.variables = variables

    def build(self):
        """Logic to handle the job."""
        return (
            self.subject('Subject Line')
            .send_from('admin@example.com')
            .reply_to('service@example.com')
            .to(self._to)
            .view('emails/welcome', self.variables)
        )
