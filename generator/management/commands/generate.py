from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import color_style
from django.conf import settings
from optparse import make_option
import os

class Command(BaseCommand):
    help = "Creates a new template schema migration for the given app"
    __help = """
    Generate:
      controller
      model
      scaffold
    """

    def handle(self, *args, **options):
        usage = "Usage: ./manage.py generate <generate_type> [MODEL_NAME] <app_name> [FIELDS]"

        PROJECT_ROOT = os.getcwd()
        INSTALLED_APPS = settings.INSTALLED_APPS
