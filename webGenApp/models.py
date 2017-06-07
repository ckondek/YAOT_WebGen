from django.db import models

class Show(models.Model):
    showName = models.CharField(max_length=15, unique=True,)

    def __str__(self):
        return self.showName

class Person(models.Model):
    base1='images/base1.jpg'
    base2='images/base2.jpg'
    base3='images/base3.jpg'
    picChoices=((base1,'pic1'),(base2,'pic2'),(base3,'pic3'))
    show = models.ForeignKey(Show, default=1)
    firstName = models.CharField(max_length=128, )
    lastName = models.CharField(max_length=128, )
    twitter = models.CharField(max_length=128, unique = True)
    email_1 = models.EmailField(max_length=128, unique = True, null = True, blank = True)
    email_2 = models.EmailField(max_length=128, unique = True, null = True, blank = True)
    link_1 = models.URLField(null = True, blank = True)
    link_2 = models.URLField(null = True, blank = True)
    picture = models.ImageField(upload_to='profilePics',blank=True)
    picChoice=models.CharField(max_length=25,choices=picChoices, default=base2)

    def __str__(self):
        return self.firstName +"_"+ self.lastName

    def give(self):
        return({'firstName':self.firstName,
                'lastName':self.lastName,
                'twitter':self.twitter,
                'email_1':self.email_1,
                'email_2':self.email_2,
                'link_1':self.link_1,
                'link_2':self.link_2})
