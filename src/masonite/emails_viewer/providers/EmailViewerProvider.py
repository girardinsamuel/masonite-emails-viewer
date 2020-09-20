"""A EmailViewerProvider Service Provider."""
import os
from masonite.provider import ServiceProvider
from masonite.emails_viewer import InstallCommand

package_directory = os.path.dirname(os.path.realpath(__file__))


class EmailViewerProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("InstallCommand", InstallCommand)

    def boot(self):
        """Boots services required by the container."""
        # compiled assets path
        public_path = os.path.join(package_directory, "../public")
        # publish assets for the app
        # when releasing package, assets are compiled into this directory
        self.publishes(
            {
                os.path.join(
                    public_path, "app.css"
                ): "storage/static/app.css",
                os.path.join(public_path, "app.js"): "storage/static/js/app.js",
            },
            tag="assets",
        )
