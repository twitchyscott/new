from __future__ import unicode_literals

from django.db import models

import random
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class House(Base):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(Base):
    name = models.CharField(max_length=254)
    cult = models.ForeignKey(House)


def build_houses():
    houses = ["Thunderbird", "Wampus", "Hordned serpent", "Pukwudgie"]
    for house in houses:
        neo=House(name=house)
        neo.save()

def build_students():
    names = [
        'alan',
        "brian",
        "scott",
        'bob',
        'dan',
        'bill',
    ]
    houses = House.objects.all()
    for name in names:
        neo = Student(name=n)
        h = houses[random.randint(0,3)]
        neo.cult = h
        neo.save()
