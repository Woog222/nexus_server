from django.test import TestCase
import logging

from .models import Person

logger = logging.getLogger(__name__)

class DBTest(TestCase):
    
    def setUp(self):
       pass
       
       
    def test_db(self):
        a = Person(name = "a")
        b = Person(name = "b")
        
        self.assertEqual(Person.objects.count(), 0)
        a.save(); b.save();
        self.assertEqual(Person.objects.count(), 2) 
        self.assertEqual(Person.objects.filter(name= "c").count(), 0)
        
        c = Person.objects.get(name="a")
        c.name = "c"
        c.save()
        self.assertEqual(Person.objects.count(), 2) 
        self.assertEqual(Person.objects.filter(name= "c").count(), 1)
        
        Person.objects.filter(name="c").delete()
        self.assertEqual(Person.objects.count(), 1) 
        self.assertEqual(Person.objects.filter(name= "c").count(), 0)
        
        Person.objects.filter(name="b").delete()
        self.assertEqual(Person.objects.count(), 0)
        
    def test_log(self):
        
        logger.info("hi")
        logger.warning("warning!")