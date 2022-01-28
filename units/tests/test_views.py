from django.test import TestCase
from django.contrib.auth.models import User

from units.models import Unit, Coordinator, Lecturer
# from students.models import Student

from django.urls import reverse


class LoanedBookInstancesByUserListViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user3 = User.objects.create_user(username='testuser3', password='KGRE8GNK32N2ER')

        test_user1.save()
        test_user2.save()
        test_user3.save()

        test_coordinator = Coordinator.objects.create(user=test_user1, title='Dr.')
        test_lecturer = Lecturer.objects.get_or_create(user=test_user2, title='Mr.')
        # Create a Unit
        test_unit = Unit.objects.create(
            title='unit1',
            code='UUUU1111',
            coordinator=test_coordinator,
            summary='this unit',
            availability='ns',
        )
        test_unit.lecturer.set(test_lecturer)

        # student1 = Student.objects.get_or_create(user=test_user3)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('index'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'index.html')
