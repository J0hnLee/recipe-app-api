"""
Test custom Django management commands.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """
    Test custom Django management commands.
    """

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patch_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [Psycopg2Error]*2 + \
            [OperationalError]*3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

    # def test_wait_for_db_command(self):
    #     """
    #     Test the wait_for_db management command.
    #     """
    #     with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
    #         gi.side_effect = [Psycopg2Error()]
    #         with self.assertRaises(OperationalError):
    #             call_command('wait_for_db')

    # def test_create_user_command(self):
    #     """
    #     Test the create_user management command.
    #     """
    #     call_command('create_user', '
