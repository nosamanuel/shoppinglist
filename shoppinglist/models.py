from django.db import models

LEVEL_CHOICES = {
        'E': 'Empty',
        'L': 'Low',
        'F': 'Full',
    }

VOTE_CHOICES = {
        -1: '-1',
        0: '',
        1: '+1',
    }

class Ingredient(models.Model):
    name = models.CharField(max_length=1024)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES.items())

    def __unicode__(self):
        return u'%s - %s' % (self.name, LEVEL_CHOICES[self.level])


class Purchase(models.Model):
	ingredient = models.ForeignKey(Ingredient, related_name='purchases')
	purchaser = models.ForeignKey('auth.User', related_name='purchases')
    cost = models.DecimalField(blank=True, null=True)
    date = models.DateField(auto_add_now=True)

	def __unicode__(self):
		return '%s purchased by %s' % (self.ingredient, self.purchaser)


class List(models.Model):
    name = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_add_now=True)


class Item(models.Model):
    ingredient = models.ForeignKey(Ingredient)


class Vote(models.Model):
    item = models.ForeignKey(Item, related_name='votes')
    user = models.ForeignKey('auth.User', related_name='votes')
    vote = models.IntegerField(choices=VOTE_CHOICES.items())
