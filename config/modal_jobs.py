import os

import django
import modal

from config import image, mounts, secrets

# the parameter passed to Stub will be the name of the container
stub = modal.Stub(name="jobs")

schedule = modal.Period(hours=1)


@stub.function(schedule=schedule, secret=secrets, image=image, mounts=mounts)
def handle_command():

    os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="config.modal_settings")
    django.setup()

    from core.management.commands.jobs import JobsCommand

    command = JobsCommand()
    command.handle()
