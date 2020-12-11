from django.db import models

# Create your models here.


class MainPage(models.Model):
    main_title = models.CharField(max_length=256, null=True, blank=True)
    main_info = models.TextField(null=True, blank=True)
    main_name = models.CharField(max_length=256, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    main_logo = models.FileField(null=True, blank=True)
    facebook_link = models.CharField(max_length=256, null=True, blank=True)
    facebook_icon = models.CharField(max_length=256, null=True, blank=True)
    instagram_link = models.CharField(max_length=256, null=True, blank=True)
    instagram_icon = models.CharField(max_length=256, null=True, blank=True)
    google_link = models.CharField(max_length=256, null=True, blank=True)
    google_icon = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class Menu(models.Model):
    menu_name = models.CharField(max_length=256, null=True, blank=True)
    link = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class About(models.Model):
    about_title = models.CharField(max_length=256, null=True, blank=True)
    about_image = models.FileField(null=True, blank=True)
    about_info = models.TextField(null=True, blank=True)
    about_name = models.CharField(max_length=256, null=True, blank=True)
    name_info = models.CharField(max_length=256, null=True, blank=True)
    about_age = models.CharField(max_length=256, null=True, blank=True)
    age_info = models.IntegerField(blank=True, null=True)
    about_experience = models.CharField(max_length=256, null=True, blank=True)
    experience_info = models.CharField(max_length=256, null=True, blank=True)
    about_country = models.CharField(max_length=256, null=True, blank=True)
    country_info = models.CharField(max_length=256, null=True, blank=True)
    about_location = models.CharField(max_length=256, null=True, blank=True)
    location_info = models.CharField(max_length=256, null=True, blank=True)
    about_email = models.CharField(max_length=256, null=True, blank=True)
    email_info = models.CharField(max_length=256, null=True, blank=True)
    about_phone = models.CharField(max_length=256, null=True, blank=True)
    phone_info = models.CharField(max_length=256, null=True, blank=True)
    download_btn = models.CharField(max_length=256, null=True, blank=True)
    db_info = models.CharField(max_length=256, null=True, blank=True)
    contact_btn = models.CharField(max_length=256, null=True, blank=True)
    cb_info = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = "About Item"
        verbose_name_plural = "About Items"


class Service(models.Model):
    service_head = models.CharField(max_length=256, null=True, blank=True)
    backend_title = models.CharField(max_length=256, null=True, blank=True)
    backend_info = models.TextField(null=True, blank=True)
    marketing_title = models.CharField(max_length=256, null=True, blank=True)
    marketing_info = models.TextField(null=True, blank=True)
    brand_title = models.CharField(max_length=256, null=True, blank=True)
    brand_info = models.TextField(null=True, blank=True)
    consult_title = models.CharField(max_length=256, null=True, blank=True)
    consult_info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.service_head

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Service Items"


class Resume(models.Model):
    resume_head = models.CharField(max_length=256, null=True, blank=True)
    resume_title = models.CharField(max_length=256, null=True, blank=True)
    resume_year = models.CharField(max_length=256, null=True, blank=True)
    resume_info = models.TextField(null=True, blank=True)
    resume_college = models.CharField(max_length=256, null=True, blank=True)
    college_year = models.CharField(max_length=256, null=True, blank=True)
    college_info = models.TextField(null=True, blank=True)
    resume_school = models.CharField(max_length=256, null=True, blank=True)
    school_year = models.CharField(max_length=256, null=True, blank=True)
    school_info = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.resume_head

    class Meta:
        verbose_name = "Resume Item"
        verbose_name_plural = "Resume Items"


class Work(models.Model):
    work_title = models.CharField(max_length=256, null=True, blank=True)
    btn_all = models.CharField(max_length=256, null=True, blank=True)
    btn_backend = models.CharField(max_length=256, null=True, blank=True)
    btn_brand = models.CharField(max_length=256, null=True, blank=True)
    btn_market = models.CharField(max_length=256, null=True, blank=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)
    img4 = models.FileField(null=True, blank=True)
    img5 = models.FileField(null=True, blank=True)
    img6 = models.FileField(null=True, blank=True)
    num1 = models.IntegerField(null=True, blank=True)
    num2 = models.IntegerField(null=True, blank=True)
    num3 = models.IntegerField(null=True, blank=True)
    num4 = models.IntegerField(null=True, blank=True)
    comment1 = models.CharField(max_length=256, null=True, blank=True)
    comment2 = models.CharField(max_length=256, null=True, blank=True)
    comment3 = models.CharField(max_length=256, null=True, blank=True)
    comment4 = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.work_title

    class Meta:
        verbose_name = "Work Item"
        verbose_name_plural = "Work Items"


class Contact(models.Model):
    contact_form = models.CharField(max_length=256, null=True, blank=True)
    contact_address = models.CharField(max_length=256, null=True, blank=True)
    btn_send = models.CharField(max_length=256, null=True, blank=True)
    map = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.contact_form

    class Meta:
        verbose_name = "Contact Item"
        verbose_name_plural = "Contact Items"


class FormCreate(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    subject = models.CharField(max_length=256, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Form Item"
        verbose_name_plural = "Form Items"