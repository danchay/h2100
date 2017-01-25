from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShURL 


class Command(BaseCommand):
    help = 'Refreshes all ShURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

        # The double-dash "--items" above makes it so that items is not required as
        # a command argument.


    def handle(self, *args, **options):
        return ShURL.objects.refresh_shortcodes(items=options['items'])
