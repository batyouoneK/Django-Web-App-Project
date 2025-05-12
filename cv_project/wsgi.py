"""
cv_project projesi için WSGI yapılandırması.

``application`` adlı modül seviyesinde bir değişken olarak WSGI çağrılabilir bileşenini dışa açar.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_project.settings')

application = get_wsgi_application()