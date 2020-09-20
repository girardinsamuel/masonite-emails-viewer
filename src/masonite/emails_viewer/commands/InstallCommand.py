"""A InstallCommand Command."""
import os
from cleo import Command
from masonite.packages import create_controller, create_or_append_config, append_web_routes

package_directory = os.path.dirname(os.path.realpath(__file__))

import os
import shutil

# TODO: add this helper in Masonite core
def create_view(location, to='resources/templates/emails_preview'):
    file_name = os.path.basename(location)

    view_directory = os.path.join(os.getcwd(), to)
    view_file = os.path.join(view_directory, file_name)
    if not os.path.exists(view_directory):
        # Create the path to the model if it does not exist
        os.makedirs(view_directory)

    if os.path.isfile(view_file):
        # if file does exist
        print('\033[91m{0} File Already Exists!\033[0m'.format(file_name))
    else:
        # copy file over
        shutil.copyfile(
            location,
            view_file
        )

        print('\033[92m{0} File Created\033[0m'.format(file_name))


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
                '../templates/index.html'
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
