import os

import modal
from django.core.wsgi import get_wsgi_application

from . import image, mounts, secrets

# the name parameter passed to Stub will be the name of the app
# in the modal dashboard
stub = modal.Stub(name='web')


@stub.wsgi(label='django-example', image=image, secret=secrets, mounts=mounts)
def app():
    # the label argument of this function will be part of the url
    # this label will result in https://<workspace name>--django-example.modal.run

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.modal_settings")

    # application instance must be created in this decorated function
    # in order to access secret values like SECRET_KEY
    application = get_wsgi_application()

    return application


if __name__ == "__main__":
    stub.serve()
