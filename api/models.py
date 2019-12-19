from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)
	points = models.PositiveIntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uservendor')

class Card(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercard')
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendors')

	def __str__(self):
		return self.user.username

class Point(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='cardpoint')
	
class Reward(models.Model):
	redeemed = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
	redeem_date = models.DateTimeField(null=True, blank=True)
	card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='cardreward')


# class RedeemedReward(models.Model):
#...future