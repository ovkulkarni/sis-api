"""
Django settings for sis_api project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9hd7+_(7l$984*fb5gd5*52kn*n9x)-3ce=c925&v)1-u4zu$l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "FALSE").upper() == "TRUE"

TEST_USER = "1234567"
TEST_GRADE_DATA = {
    "courses": [
        {
            "teacher": "APUSH Teacher",
            "period": 1,
            "name": "AP US History (231905)",
            "grades": {
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "assignments": [],
            "location": "1"
        },
        {
            "teacher": "English Teacher",
            "period": 2,
            "name": "English 11 (1150T1)",
            "grades": {
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "assignments": [
                {
                    "score": "Not Due",
                    "assignment_type": "Summative",
                    "name": "Presentation",
                    "points": "75 Points Possible",
                    "due_date": "2018-03-06",
                    "date": "2018-01-09",
                    "notes": ""
                }
            ],
            "location": "2"
        },
        {
            "teacher": "German Teacher",
            "period": 3,
            "name": "AP German Lang (527004)",
            "grades": {
                "third_quarter": {
                    "letter": "B-",
                    "percentage": "80.0"
                }
            },
            "assignments": [
                {
                    "score": "16 out of 20",
                    "assignment_type": "Formative Assessment",
                    "name": "Vocab Quiz",
                    "points": "16 / 20",
                    "due_date": "2018-02-06",
                    "date": "2018-02-06",
                    "notes": ""
                }
            ],
            "location": "3"
        },
        {
            "teacher": "Math Teacher",
            "period": 4,
            "name": "AP Calculus BC (317704)",
            "grades": {
                "third_quarter": {
                    "letter": "A",
                    "percentage": "95.0"
                }
            },
            "assignments": [
                {
                    "score": "95 out of 100",
                    "assignment_type": "Test",
                    "name": "Chapter 6 Test",
                    "points": "95 / 100",
                    "due_date": "2018-01-02",
                    "date": "2018-01-02",
                    "notes": ""
                }
            ],
            "location": "4"
        },
        {
            "teacher": "CS Teacher",
            "period": 5,
            "name": "ParallelComputing2 (3199T2)",
            "grades": {
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "assignments": [],
            "location": "5"
        },
        {
            "teacher": "Physics Teacher",
            "period": 6,
            "name": "AP Physics C M&EM (457004)",
            "grades": {
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "200.0"
                }
            },
            "assignments": [
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 25 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 26 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 27 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 28 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 29 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "Not Graded",
                    "assignment_type": "Quiz",
                    "name": "Ch 30 Quiz",
                    "points": "15 Points Possible",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                },
                {
                    "score": "2 out of 30",
                    "assignment_type": "Test",
                    "name": "SLOBS",
                    "points": "2 / 0",
                    "due_date": "2018-02-09",
                    "date": "2018-02-09",
                    "notes": ""
                }
            ],
            "location": "6"
        },
        {
            "teacher": "CS Teacher",
            "period": 7,
            "name": "Artificial Intell2 (319967)",
            "grades": {
                "third_quarter": {
                    "letter": "A",
                    "percentage": "100.0"
                }
            },
            "assignments": [
                {
                    "score": "Not Due",
                    "assignment_type": "Quarter",
                    "name": "Lab C",
                    "points": "10 Points Possible",
                    "due_date": "2018-02-13",
                    "date": "2018-02-13",
                    "notes": ""
                },
                {
                    "score": "Not Due",
                    "assignment_type": "Quarter",
                    "name": "Lab B",
                    "points": "5 Points Possible",
                    "due_date": "2018-02-12",
                    "date": "2018-02-12",
                    "notes": ""
                },
                {
                    "score": "7 out of 7",
                    "assignment_type": "Quarter",
                    "name": "Lab A",
                    "points": "7 / 7",
                    "due_date": "2018-02-08",
                    "date": "2018-02-08",
                    "notes": ""
                },
                {
                    "score": "1 out of 1",
                    "assignment_type": "Quarter",
                    "name": "Lab A graph",
                    "points": "3 / 3",
                    "due_date": "2018-02-05",
                    "date": "2018-02-05",
                    "notes": ""
                }
            ],
            "location": "7"
        }
    ],
    "index": "2",
    "start_date": "2018-01-30",
    "name": "Third Quarter",
    "end_date": "2018-04-13"
}
TEST_REPORT_CARD_DATA = {
    "courses": [
        {
            "teacher": "APUSH Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A-",
                    "percentage": "90.9"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "B+",
                    "percentage": "89.4"
                },
                "first_semester": {
                    "letter": "A-",
                    "percentage": "90.2"
                },
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "period": 1,
            "name": "AP US History (231905)",
            "location": "1"
        },
        {
            "teacher": "English Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A",
                    "percentage": "96.1"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "A-",
                    "percentage": "90.8"
                },
                "first_semester": {
                    "letter": "A",
                    "percentage": "93.5"
                },
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "period": 2,
            "name": "English 11 (1150T1)",
            "location": "2"
        },
        {
            "teacher": "German Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A",
                    "percentage": "93.1"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "A",
                    "percentage": "93.5"
                },
                "first_semester": {
                    "letter": "A",
                    "percentage": "93.3"
                },
                "third_quarter": {
                    "letter": "B-",
                    "percentage": "80.0"
                }
            },
            "period": 3,
            "name": "AP German Lang (527004)",
            "location": "61"
        },
        {
            "teacher": "Math Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "B+",
                    "percentage": "89.1"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "B+",
                    "percentage": "88.5"
                },
                "first_semester": {
                    "letter": "B+",
                    "percentage": "89.1"
                },
                "third_quarter": {
                    "letter": "A",
                    "percentage": "95.0"
                }
            },
            "period": 4,
            "name": "AP Calculus BC (317704)",
            "location": "4"
        },
        {
            "teacher": "CS Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A",
                    "percentage": "99.3"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "A",
                    "percentage": "99.5"
                },
                "first_semester": {
                    "letter": "A",
                    "percentage": "99.4"
                },
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "period": 5,
            "name": "ParallelComputing1 (3199T1)",
            "location": "5"
        },
        {
            "teacher": "Physics Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A",
                    "percentage": "107.7"
                },
                "fourth_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                },
                "first_quarter": {
                    "letter": "C",
                    "percentage": "75.5"
                },
                "first_semester": {
                    "letter": "A-",
                    "percentage": "90.6"
                },
                "third_quarter": {
                    "letter": "N/A",
                    "percentage": "0.0"
                }
            },
            "period": 6,
            "name": "AP Physics C M&EM (457004)",
            "location": "6"
        },
        {
            "teacher": "CS Teacher",
            "grades": {
                "second_quarter": {
                    "letter": "A",
                    "percentage": "95.5"
                },
                "fourth_quarter": {
                    "letter": "A",
                    "percentage": "100.0"
                },
                "first_quarter": {
                    "letter": "A",
                    "percentage": "92.5"
                },
                "first_semester": {
                    "letter": "A",
                    "percentage": "95.5"
                },
                "third_quarter": {
                    "letter": "A",
                    "percentage": "100.0"
                }
            },
            "period": 7,
            "name": "Artificial Intell1 (319966)",
            "location": "7"
        }
    ]
}
TEST_YEAR_DATA = {
    "quarters": [
        {
            "index": "0",
            "start_date": "2017-08-28",
            "name": "First Quarter",
            "end_date": "2017-11-03"
        },
        {
            "index": "1",
            "start_date": "2017-11-08",
            "name": "Second Quarter",
            "end_date": "2018-01-25"
        },
        {
            "index": "2",
            "start_date": "2018-01-30",
            "name": "Third Quarter",
            "end_date": "2018-04-13"
        },
        {
            "index": "3",
            "start_date": "2018-04-17",
            "name": "Final",
            "end_date": "2018-06-15"
        }
    ]
}
TEST_USER_DATA = {
    "school_name": "Jefferson Sci/Tech High School",
    "grade": 11,
    "username": "1234567",
    "photo": "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NRCLoAJA7e3l8S9lp9jbjXqxsZmekjQ01PsOm6dvAQzdHhr6zB0aGtwJQHIBWBM+OpsPKxT7x6LkCj/RP4iTAsCJDYH8AAAAIGNIUk0AAFkJAABVSAAA98wAAIBVAABlcAAA1PcAAC1IAAAUnAf5JBQAAAAJcEhZcwAACxMAAAsTAQCanBgAAAoWaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIgogICAgICAgICAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8cGhvdG9zaG9wOklDQ1Byb2ZpbGU+RGlzcGxheTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4yNTY8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjY1NTM1PC9leGlmOkNvbG9yU3BhY2U+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yNTY8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICAgICA8ZGM6Zm9ybWF0PmltYWdlL3BuZzwvZGM6Zm9ybWF0PgogICAgICAgICA8eG1wOk1ldGFkYXRhRGF0ZT4yMDE1LTA0LTAyVDAxOjI3OjA4KzA4OjAwPC94bXA6TWV0YWRhdGFEYXRlPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAxNS0wNC0wMlQwMToyNzowOCswODowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDE1LTA0LTAyVDAxOjI3OjA4KzA4OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgQ0MgKE1hY2ludG9zaCk8L3htcDpDcmVhdG9yVG9vbD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDE1LTA0LTAyVDAxOjI3OjA4KzA4OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjdkM2UwMjRjLWJkNTUtNDE2Yi05OTBiLWQxYmQ1Njk4ZTk0YTwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIENDIChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDE1LTA0LTAyVDAxOjI3OjA4KzA4OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmIyYTE4Yzk1LTMyMWYtNDI3Yy1hNTcxLTgxNTY5YmJkMjAyZDwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDx4bXBNTTpJbnN0YW5jZUlEPnhtcC5paWQ6YjJhMThjOTUtMzIxZi00MjdjLWE1NzEtODE1NjliYmQyMDJkPC94bXBNTTpJbnN0YW5jZUlEPgogICAgICAgICA8eG1wTU06T3JpZ2luYWxEb2N1bWVudElEPnhtcC5kaWQ6N2QzZTAyNGMtYmQ1NS00MTZiLTk5MGItZDFiZDU2OThlOTRhPC94bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPnhtcC5kaWQ6N2QzZTAyNGMtYmQ1NS00MTZiLTk5MGItZDFiZDU2OThlOTRhPC94bXBNTTpEb2N1bWVudElEPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAg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",
    "full_name": "Test User",
    "schedule": [
        {
            "teacher": "APUSH Teacher",
            "period": 1,
            "name": "AP US History",
            "location": "1"
        },
        {
            "teacher": "English Teacher",
            "period": 2,
            "name": "English 11",
            "location": "2"
        },
        {
            "teacher": "German Teacher",
            "period": 3,
            "name": "AP German Lang",
            "location": "3"
        },
        {
            "teacher": "Math Teacher",
            "period": 4,
            "name": "AP Calculus BC",
            "location": "4"
        },
        {
            "teacher": "CS Teacher",
            "period": 5,
            "name": "ParallelComputing2",
            "location": "5"
        },
        {
            "teacher": "Physics Teacher",
            "period": 6,
            "name": "AP Physics C M&EM",
            "location": "6"
        },
        {
            "teacher": "CS Teacher",
            "period": 7,
            "name": "Artificial Intell2",
            "location": "202"
        },
        {
            "teacher": "Homeroom Teacher",
            "period": 8,
            "name": "Homeroom Grade 11",
            "location": "285"
        }
    ]
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from .secret import *
except ImportError:
    pass

ALLOWED_HOSTS = ["sisapi.sites.tjhsst.edu", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'fcm_django',
    'base',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sis_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'caches',
    }
}

WSGI_APPLICATION = 'sis_api.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'base.backends.SISAuthBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'base.backends.SISBasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": FCM_SERVER_KEY,
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": True,
}

AUTH_USER_MODEL = 'base.User'
