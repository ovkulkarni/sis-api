from django.core.cache import cache
from django.core.management.base import BaseCommand
from base.helpers import get_quarter_grades
from base.models import User
from multiprocessing import Pool
from rest_framework.renderers import JSONRenderer
from json import loads


class FakeRequest(object):
    def __init__(self, user, password=None, force=False):
        self.user = user
        self.session = {}
        if password:
            self.session.update({'password': password})
        self.GET = {'force': force}


def check_user_updates(user):
    print("Checking for updates for {}".format(user))
    devices = user.fcmdevice_set.filter(active=True)
    key = "{}:{}".format(user.username, "Current")
    cached = cache.get(key)
    new_grades = get_quarter_grades(FakeRequest(user, force=True), "", "")
    if cached:
        for i in range(len(new_grades['courses'])):
            course = new_grades['courses'][i]
            for assignment in course['assignments']:
                if assignment not in cached['courses'][i]['assignments']:
                    for device in devices:
                        device.send_message(data={'title': "Grade Posted: {}".format(course['name'].split("(")[0].strip()),
                                                  'body': "{}: {}".format(assignment['name'], assignment['score']),
                                                  'extra': JSONRenderer().render(course).decode("utf-8")
                                                  })
                        print('Sent notification to {}, device {}'.format(device.user.username, device.registration_id))


class Command(BaseCommand):
    help = 'Runs notifications for updates in grades'

    def handle(self, *args, **options):
        with Pool(4) as pool:
            pool.map(check_user_updates, User.objects.filter(encrypted_password__isnull=False))
        print('Successfully finished sending notifications')
