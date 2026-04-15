import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import RequestFactory
from home.views import home
from django.contrib.auth.models import User

req = RequestFactory().get('/')
# Create or get a user to bypass login_required
user, _ = User.objects.get_or_create(username='testviewuser')
req.user = user

try:
    response = home(req)
    print("STATUS CODE:", response.status_code)
    print("CONTENT LENGTH:", len(response.content))
    content = response.content.decode('utf-8')
    if len(content) < 1000:
        print("CONTENT:")
        print(content)
except Exception as e:
    import traceback
    print("Exception occurred:")
    traceback.print_exc()
