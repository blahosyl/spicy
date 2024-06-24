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
        # comment setup rewritten with the help of tutor Roo
        self.comment = Comment.objects.create( 
            recipe=self.recipe, 
            author=self.user1, 
            body="Comment for deletion" )
        # self.comment.save()

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
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    # this needs more work
    # def test_successful_comment_editing(self):
    #     """Test for successfully editing a comment"""
    #     # Logged-in user is the comment author
    #     self.client.login(
    #         username="user1Name", password="user1Password")
    #     comment_data = {
    #         'author': 'user1',
    #         'body': 'Edited comment.'
    #     }
    #     response = self.client.post(reverse(
    #         'recipe_detail', args=['recipe-title']), comment_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotIn(
    #         b'Comment for deletion',
    #         response.content
    #     )
    #     self.assertIn(
    #         b'Edited comment.',
    #         response.content
    #     )

    # the following test rewritten with the help of tutor Roo
    def test_successful_comment_editing(self):
        """Test for successfully editing a comment"""
        self.client.login(
            username="user1Name", password="user1Password")
        edit_url = reverse('comment_edit', args=['recipe-title', self.comment.id])
        print(f"Edit URL: {edit_url}")
        comment_data = {
            'body': 'Edited comment.'
        }
        response = self.client.post(edit_url, comment_data)
        print(f"Response status code: {response.status_code}")
        self.comment.refresh_from_db()  # Refresh to get updated data
        print(f"Updated comment body: {self.comment.body}")
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(self.comment.body, 'Edited comment.')


    # this needs more work
    # def test_successful_comment_deletion(self):
    #     """Test for successfully deleting a comment"""
    #     self.client.login(
    #         username="user1Name", password="user1Password")
    #     self.client.post('recipe-title/delete_comment/1')
    #     response = self.client.post(reverse(
    #         'recipe_detail', args=['recipe-title']))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotIn(
    #         b'Comment for deletion',
    #         response.content
    #     )

    # # this needs more work
    # def test_unsuccessful_comment_deletion(self):
    #     """Test for failing to delete a comment belonging to another user"""
    #     self.client.login(
    #         username="user2Name", password="user2Password")
    #     print(self.comment.author.username)
    #     if self.comment.author.username == "user2Name":
    #         self.comment.delete()
    #     response = self.client.post(reverse(
    #         'recipe_detail', args=['recipe-title']))
    #     self.assertEqual(response.status_code, 403)
    #     self.assertIn(
    #         b'Comment for deletion',
    #         response.content
    #     )