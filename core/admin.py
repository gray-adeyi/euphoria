from django.contrib import admin
from . import models

####################################
#
#   INLINES
####################################
class ResumeDataInline(admin.StackedInline):
    model = models.ResumeData
    extra = 1

class SiteSocialAccountInline(admin.StackedInline):
    model = models.SiteSocialAccount
    extra = 1

class ResumeDataSocialAccountInline(admin.StackedInline):
    model = models.ResumeDataSocialAccount
    extra = 1

class ProfessionInline(admin.StackedInline):
    model = models.Profession
    extra = 1

class SkillInline(admin.StackedInline):
    model = models.Skill
    extra = 1

class EducationInline(admin.StackedInline):
    model = models.Education
    extra = 1

class ProfessionalExperienceInline(admin.StackedInline):
    model = models.ProfessionalExperience
    extra = 1

class ServiceInline(admin.StackedInline):
    model = models.Service
    extra = 1

class TestimonialInline(admin.StackedInline):
    model = models.Testimonial
    extra = 1

class ProjectInline(admin.StackedInline):
    model = models.Project
    extra = 1

####################################
#
#   MODEL ADMINS
####################################
@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    inlines = [
        ResumeDataInline,
        SiteSocialAccountInline,
    ]


@admin.register(models.ResumeData)
class ResumeDataAdmin(admin.ModelAdmin):
    inlines = [
        ResumeDataSocialAccountInline,
        ProfessionInline,
        SkillInline,
        EducationInline,
        ProfessionalExperienceInline,
        ServiceInline,
        TestimonialInline,
        ProjectInline,
    ]

admin.site.register(models.Message)