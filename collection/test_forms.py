# These tests were written based on the "I Think Therefore I Blog" walkthrough
# project by Code Institute https://github.com/Code-Institute-Solutions/blog

from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        """
        Test for a valid comment form
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """
        Test for an invalid comment form without a body
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')
        