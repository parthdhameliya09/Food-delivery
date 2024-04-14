from django.db import models

class State(models.Model):
    name = models.TextField(max_length=100)
    sid = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.TextField(max_length=100)
    cid = models.TextField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.TextField(max_length=100)
    aid = models.TextField(max_length=50)
    pincode = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

