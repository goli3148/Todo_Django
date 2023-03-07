from django.test import TestCase
from todo_app.models import todo

class dateTest(TestCase):
    def setUp(self):
        todo.objects.all().values()
        todo.objects.create(subject="study", extra="hi")
    
    def test_this(self):
        print(todo.objects.all().values())
        input()
        
# Create your tests here.
