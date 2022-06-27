"""
Djago command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Wait for database to be available.'
    # def add_arguments(self, parser: CommandParser) -> None:
    #     return super().add_arguments(parser)


    def handle(self, *args, **options) :
        pass

    def check(self, *args, **options) :
        pass
    # def handle(self, *args: Any, **options: Any) -> Optional[str]:
    #     return super().handle(*args, **options)