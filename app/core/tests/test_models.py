"""
Tests for models
"""

from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='user@example.com', password='test123'):
    """Create a user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """
    Tests for models
    """

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        password = 'Testpass123'
        sample_emails = [['test1@EXAMPLE.com', 'test1@example.com'], ['Test2@Example.com', 'Test2@example.com'],
                         ['TEST3@EXAMPLE.COM', 'TEST3@example.com'], ['test4@example.COM', 'test4@example.com']]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, password)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            email='test@example.com', password='Testpass123')

        recipe = models.Recipe.objects.create(user=user, title="Sample recipe name", time_minutes=5,
                                              price=Decimal('5.50'), description='Sample recipe description.', )

        self.assertEqual(recipe.title, 'Sample recipe name')

    def test_create_tag(self):
        """Test creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='tag1')
        self.assertEqual(str(tag), tag.name)
