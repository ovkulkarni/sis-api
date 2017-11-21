from django.core.cache import cache
from django.core.management.base import BaseCommand
from base.helpers import get_quarter_grades
from base.models import User
from fcm_django.models import FCMDevice


class FakeRequest(object):
    def __init__(self, user, force):
        self.user = user
        self.session = {}
        self.GET = {'force': force}


class Command(BaseCommand):
    help = 'Runs notifications for updates in grades'


    def handle(self, *args, **options):
        for user in User.objects.filter(encrypted_password__isnull=False):
            self.stdout.write("Checking for updates for {}".format(user))
            devices = FCMDevice.objects.filter(user=user)
            key = "{}:{}".format(user.username, "Current")
            cached = cache.get(key)
            new_grades = get_quarter_grades(FakeRequest(user, True), "", "")
            if cached:
                for i in range(len(new_grades['courses'])):
                    course = new_grades['courses'][i]
                    for assignment in course['assignments']:
                        if assignment not in cached['courses'][i]['assignments']:
                            for device in devices:
                                device.send_message(title="Grade Posted: {}".format(course['name']), body="{}: {}".format(assignment['name'], assignment['score']))
                                print('Sent notification to {}, device {}'.format(device.user.username, device.registration_id))
        print('Successfully finished sending notifications')
