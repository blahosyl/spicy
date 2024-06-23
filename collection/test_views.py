from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe, Comment

class TestCollectionViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="superUserName",
            password="superUserPassword",
            email="test@test.com"
        )
        self.user1 = User.objects.create_user(
            username="user1Name",
            password="user1Password",
            email="user1@test.com"
        )
        self.user2 = User.objects.create_user(
            username="user2Name",
            password="user2Password",
            email="user2@test.com"
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
                                author=self.user1,
                                body="Comment for deletion")
        self.comment.save()

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
            username="superUserName", password="superUserPassword")
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
    
    def test_successful_comment_deletion(self):
        """Test for successfully deleting a comment"""
        self.client.login(
            username="user1Name", password="user1Password")
        if self.comment.author == self.user1:
            self.comment.delete()
        response = self.client.get(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            b'Comment for deletion',
            response.content
        )

    def test_unsuccessful_comment_deletion(self):
        """Test for failing to delete a comment belonging to another user"""
        self.client.login(
            username="user2Name", password="user2password")
        if self.comment.author == self.user1:
            self.comment.delete()
        response = self.client.get(reverse(
            'recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment for deletion',
            response.content
        )