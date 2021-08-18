from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class SiteInfo(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=14, blank=True)

    def save(self, **kwargs):
        # Override the save method to limit SiteInfo instances to 1
        if SiteInfo.objects.count() < 1:
            super().save(**kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Site Info'


class ResumeData(models.Model):
    FL_OPTIONS = (
        ('Y','Available'),
        ('N', 'Unavalable'),
    )

    # TODO: Get and update the appropriate degrees :-(
    D_OPTIONS = (
        ("O","O'level"),
        ("ND","ND"),
        ("HND","HND"),
        ("BSC","B.SC"),
        ("BENG","B.ENG"),
        ("MSC","M.SC"),
        ("MENG","M.ENG"),
        ("PHD","PHD"),
    )

    user = models.ForeignKey(User, related_name='resume_data', on_delete=models.CASCADE)
    site = models.OneToOneField(SiteInfo, on_delete=models.SET_NULL, null=True, related_name='resume_data',)
    dob = models.DateField(help_text='Date of Birth', blank=True)
    bio = models.TextField(help_text='tell us something about yourself...', blank=True)
    age = models.IntegerField(blank=True)
    freelance = models.CharField(max_length=1, choices=FL_OPTIONS, blank=True)
    degree = models.CharField(max_length=8, choices=D_OPTIONS, blank=True)
    city = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    happy_clients = models.IntegerField(blank=True)
    hours_of_support = models.IntegerField(blank=True)
    awards = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} <{self.user.email}>"

    class Meta:
        verbose_name_plural = 'Resume Data'


class SocialAccount(models.Model):
    OPTIONS = (
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter <Currently Banned in Nigeria :( >'),
    )
    name = models.CharField(max_length=15, choices=OPTIONS)
    link = models.URLField()

    def __str__(self) -> str:
        return self.get_name_display()

class ResumeDataSocialAccount(models.Model):
    resume = models.ForeignKey(ResumeData, related_name='social_accounts', on_delete=models.CASCADE)

class SiteSocialAccount(models.Model):
    site = models.ForeignKey(SiteInfo, related_name='social_accounts', on_delete=models.CASCADE)

class Profession(models.Model):
    resume = models.ForeignKey(ResumeData, related_name='professions', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

    def get_prefix(self):
        """
        Returns the appropriate article i.e `A` or `An`
        for the `self.name`
        """
        vowels = ['a','e','i','o','u']
        if self.name[0].lower() in vowels:
            return 'an'
        else:
            return 'a'

class SkillManager(models.Manager):
    def even(self):
        all = self.all()
        result = [ x for x in all if x.pk % 2 == 0]
        return result

    def odd(self):
        all = self.all()
        result = [ x for x in all if x.pk % 2 != 0]
        return result

class Skill(models.Model):
    objects = SkillManager()
    resume = models.ForeignKey(ResumeData, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=3, help_text='In percentage e.g 45 (Note % excluded)', blank=True)

    def __str__(self) -> str:
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=50)
    timeframe = models.CharField(max_length=20, help_text='Expected format is `2001 - 2003`', blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Education(Experience):
    resume = models.ForeignKey(ResumeData, related_name='educations', on_delete=models.CASCADE)

class ProfessionalExperience(Experience):
    resume = models.ForeignKey(ResumeData, related_name='professional_experiences', on_delete=models.CASCADE)


class Service(models.Model):
    resume = models.ForeignKey(ResumeData, related_name='services', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField( blank=True)

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    resume = models.ForeignKey(ResumeData, related_name='testimonies', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    testimony = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    PT_OPTIONS = (
        ('wb', 'Web'),
        ('as','Automation Script'),
        ('es', 'Electrical Service'),
    )
    owner = models.ForeignKey(ResumeData, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    poster = models.ImageField(blank = True)
    link = models.URLField(blank=True)
    project_type = models.CharField(max_length=2, choices=PT_OPTIONS)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_pt_options(self):
        return [x[1] for x in  self.PT_OPTIONS]

class Message(models.Model):
    """
    This model holds contact message sent from the
    index page.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Msg from <{self.email}> subject: {self.subject}'