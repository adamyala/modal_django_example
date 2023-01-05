from django.core.management.base import BaseCommand


class JobsCommand(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("running job")
