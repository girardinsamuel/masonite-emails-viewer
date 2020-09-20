"""A InstallCommand Command."""
import os
from cleo import Command
from masonite.packages import create_controller, create_or_append_config, create_view, append_web_routes

package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Install package

    command:name
        {argument : description}
    """

    def handle(self):

        # Publish view
        create_view(
            os.path.join(
                package_directory,
                '../templates/emails_preview.html'
            )
        )


        # Publish BrowserlogController => no need to publish it ? auto-import from package ?

        # Publish config file
        create_or_append_config(
            os.path.join(
                package_directory,
                '../config/mail_preview.py'
            )
        )

        # Append route
        # with open('routes/web.py', 'a') as f:
        #     f.write("\nROUTES += [ \n")
        #     f.write("    Get('/emails', 'EmailsController@index').name('emails'),\n")
        #     f.write("    Get('/emails/@name', 'EmailsController@detail').name('emails.detail'),\n")
        #     f.write("    Post('/emails/@name/send', 'EmailsController@send').name('emails.send'),\n")
        #     f.write(']\n')
        # OR
        append_web_routes(os.path.join('../routes/web.py'))
