#models.py

form django.db import models

class MaleManager(models.Manager):
  def get_query_set(self):
    return super(MaleManager, self).get_query_set().filter(sex='M')
    
class FemaleManager(models.Manager):
  def get_query_set(self):
    return super(FemaleManager, self).get_query_set().filter(sex='F')
 
 class person(models.Model):
  first_name=models.CharFiel(max_length=10)
  last_name=models.CharFiel(max_length=10)
  sex=models.CharFiel(max_length=1, choices=(('M', 'Male'),('F', 'Female')))
  men=Malemanager()
  women=FemaleManager()
  
