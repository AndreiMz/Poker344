import random
from django import template
from faker import Faker

register = template.Library()

@register.simple_tag
def random_int(a, b=None):
		if b is None:
			a, b =0, a
		return random.randint(a,b)

@register.simple_tag
def random_exp(a=0):
	exp = ['Begginer', 'Intermediate', 'Tutorial Room', 'Advanced']
	return exp[random.randint(0,3)]

@register.simple_tag
def random_name(a=0):
	fake = Faker()
	return fake.company()