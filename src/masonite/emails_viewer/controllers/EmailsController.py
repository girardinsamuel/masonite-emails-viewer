"""A EmailsController Module."""
import os
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.helpers import config
from masonite.drivers import Mailable
from masonite import Mail
import importlib


def get_mail_class(name):
    module = importlib.import_module('app.mailable.' + name)
    mail_class = getattr(module, name)
    return mail_class


class EmailsController(Controller):
    """EmailsController Controller Class."""

    def __init__(self, request: Request):
        """EmailsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        self.mailables_dir = os.path.join(config('application.base_directory'), 'app', 'mailable')

    def index(self, view: View):
        
        # get config related to emails viewer package
        settings = {
            'MAILABLE_DIR': 'mailable', # config('mail_preview.dir'),
            'MAIL_DRIVER': config('mail.driver'),
        }
        # retrieve all Mailable
        emails = []
        for root, dirs, files in os.walk(self.mailables_dir):
            for file in files:
                if file.endswith(".py"):  # and is a Mailable instance
                    name = file[:-3]
                    mail_class = get_mail_class(name)
                    if issubclass(mail_class, Mailable):
                        emails.append({
                            'name': name,
                            'path': os.path.join(root, file)
                        })

        return view.render('emails', {'emails': emails, 'settings': settings})

    def detail(self, view: View, mail: Mail):
        name = self.request.param('name')
        mail_class = get_mail_class(name)
        if not issubclass(mail_class, Mailable):
            self.request.back()
        # TODO: load default parameters if no query parameters, update Mailable to store variables example
        if self.request.all_query():
            variables = self.request.all_query()
        else:
            variables = mail_class.placeholder_variables
        email = mail.mailable(mail_class('user@example.com', variables))
        return {
            'text': email.text_content,
            'html': email.html_content,
            'default_params': mail_class.placeholder_variables
        }

    def send(self, view: View, mail: Mail):
        name = self.request.param('name')
        mail_class = get_mail_class(name)
        if not issubclass(mail_class, Mailable):
            self.request.back()
        
        if self.request.all():
            variables = self.request.all()
        else:
            variables = mail_class.placeholder_variables

        mail.mailable(mail_class('user@example.com', variables)).send()
        return 'ok'
