from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe, Comment

class TestCollectionViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Recipe title", 
                         author=self.user,
                         slug="recipe-title", 
                         excerpt="Recipe excerpt",
                         instructions="Recipe instructions",
                         prep_time="10",
                         cook_time="10",
                         published=True)
        self.recipe.save()
        self.comment = Comment(id=1,
                                recipe=self.recipe,
                                author=self.user,
                                body="This is a comment")

    def test_render_recipe_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe title", response.content)
        self.assertIn(b"Recipe instructions", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a recipe"""
        self.client.login(
            username="myUsername", password="myPassword")
        recipe_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'recipe_detail', args=['recipe-title']), recipe_data)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    # this gives a false positive, because the modal text is in the HTML anyway
    def test_starting_comment_deletion(self):
        """Test for starting to delete a comment from a recipe
        The correct result is a modal asking to confirm deletion"""
        self.client.login(
            username="myUsername", password="myPassword")
        self.comment.delete()
        response = self.client.post(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Are you sure you want to delete your comment?',
            response.content
        )
    
    # this needs more work
    def test_confirming_comment_deletion(self):
        """Test for confirming to delete a comment from a recipe
        when the modal asking to confirm deletion"""
        self.client.login(
            username="myUsername", password="myPassword")
        self.comment.delete()
        response = self.client.get(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment deleted!',
            response.content
        )