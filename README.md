# sis-api
A JSON API for FCPS StudentVUE


## Installation instructions
```bash
git clone https://github.com/ovkulkarni/sis-api.git
```

Create `sis_api/secret.py` similar to the example below:
```python
from base.crypto import AESCipher
SIS_ENDPOINT = "https://sisstudent.fcps.edu/SVUE/Service/PXPCommunication.asmx"
SECRET_KEY = "secret"
DEBUG = True
CIPHER = AESCipher(SECRET_KEY)
FCM_SERVER_KEY = ""
```
Run the following commands
```bash
mkvirtualenv sis-api -p python3
pip install -r requirements.txt
./manage.py migrate
./manage.py createcachetable
```

***IN PRODUCTION ONLY***

Create a crontab entry similar to the one below (make sure the interval is less than 30 minutes)
```
*/20 * * * * python manage.py check_for_updates
```

## Misc. Info
- This application uses [fcm_django](http://fcm-django.readthedocs.io/en/latest/) to send notifications
- Passing `?save_password` in the `GET` querystring or the `POST` data will encrypt and save the user's password to the database so that notifications can be sent.
- Passing `?force` in the `GET` querystring will bypass the server cache and request the data from SIS
- The application utilizes HTTP Basic Auth for authentication
