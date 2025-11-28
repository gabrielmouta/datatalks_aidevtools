from django.test import TestCase
from django.urls import reverse

from todo.models import Todo


class TodoViewsTest(TestCase):
    def test_list_view_shows_todo(self):
        Todo.objects.create(title='List test')
        resp = self.client.get(reverse('todo:todo_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'List test')

    def test_create_view_post_creates_todo(self):
        resp = self.client.post(reverse('todo:todo_create'), {'title': 'Created', 'description': ''})
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='Created').exists())

    def test_mark_resolved_sets_flag_and_redirects(self):
        t = Todo.objects.create(title='Resolve me', resolved=False)
        resp = self.client.get(reverse('todo:todo_resolve', args=[t.pk]))
        self.assertEqual(resp.status_code, 302)
        t.refresh_from_db()
        self.assertTrue(t.resolved)
