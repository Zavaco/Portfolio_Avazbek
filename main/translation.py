from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MainPageTranslationOptions(TranslationOptions):
    fields = ('main_title', 'main_info',)


translator.register(MainPage, MainPageTranslationOptions)


class MenuTranslationOptions(TranslationOptions):
    fields = ('menu_name',)


translator.register(Menu, MenuTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = (
        'about_title',
        'about_info',
        'about_name',
        'name_info',
        'about_age',
        'about_experience',
        'experience_info',
        'about_country',
        'country_info',
        'about_location',
        'location_info',
        'about_phone',
        'download_btn',
        'contact_btn',
    )


translator.register(About, AboutTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'service_head',
        'backend_title',
        'backend_info',
        'marketing_title',
        'marketing_info',
        'brand_title',
        'brand_info',
        'consult_title',
        'consult_info',

    )


translator.register(Service, ServiceTranslationOptions)


class ResumeTranslationOptions(TranslationOptions):
    fields = (
        'resume_head',
        'resume_title',
        'resume_info',
        'resume_college',
        'college_info',
        'resume_school',
        'school_info',

    )


translator.register(Resume, ResumeTranslationOptions)


class WorkTranslationOptions(TranslationOptions):
    fields = (
        'work_title',
        'btn_all',
        'btn_backend',
        'btn_brand',
        'btn_market',
        'comment1',
        'comment2',
        'comment3',
        'comment4',

    )


translator.register(Work, WorkTranslationOptions)


class ContactTranslationOptions(TranslationOptions):
    fields = (
        'contact_form',
        'contact_address',
        'btn_send',
        'map',

    )


translator.register(Contact, ContactTranslationOptions)