from django.test import TestCase

from todo.models import Todo


class TodoModelTest(TestCase):
    def test_create_and_str_and_mark_resolved(self):
        t = Todo.objects.create(title='Test todo', description='desc')
        self.assertEqual(str(t), 'Test todo')
        self.assertFalse(t.resolved)
        t.mark_resolved()
        t.refresh_from_db()
        self.assertTrue(t.resolved)
