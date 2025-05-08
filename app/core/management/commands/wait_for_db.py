"""
Django command to wait for DB to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for DB"""
    def handle(self, *args, **options):
        """ENtry point for command"""
        self.stdout.write('Waiting fro database ...') 
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default']) # type: ignore
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('database, unavailable waiting 1 second ')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!')) # type: ignore

