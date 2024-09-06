import os

import django
import modal

from config import image, mounts, secrets

# the parameter passed to App will be the name of the container
app = modal.App(name="jobs")

schedule = modal.Period(hours=1)


@app.function(schedule=schedule, secrets=secrets, image=image, mounts=mounts)
def handle_command():

    os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="config.modal_settings")
    django.setup()

    from core.management.commands.jobs import JobsCommand

    command = JobsCommand()
    command.handle()
