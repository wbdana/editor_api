from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Owner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Collaborator(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


class Reader(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)


@receiver(post_save, sender=User)
def create_user_roles(sender, instance, created, **kwargs):
    """
    Creates an associated Owner, Collaborator, and Reader profile (role) for each User.
    :param sender: User model
    :param instance: User instance
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Owner.objects.create(user=instance)
        Collaborator.objects.create(user=instance)
        Reader.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_roles(sender, instance, **kwargs):
    """
    Updates associated Owner, Collaborator, and Reader roles for each User when User is saved.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.owner.save()
    instance.collaborator.save()
    instance.reader.save()


class Record(models.Model):
    """
    Example file: src/components/Navbar.jsx
    name: 'Navbar'
    extension: '.jsx'
    path: 'src/components'
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    extension = models.CharField(max_length=100, blank=True, default='')
    path = models.CharField(max_length=500, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey(Owner, related_name='records', on_delete=models.CASCADE, default='1')
    collaborators = models.ManyToManyField(Collaborator, related_name='records')
    readers = models.ManyToManyField(Reader, related_name='records')

    class Meta:
        ordering = ('created',)
