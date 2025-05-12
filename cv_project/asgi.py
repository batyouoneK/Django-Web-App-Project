"""
cv_project projesi için ASGI yapılandırması.

``application`` adlı modül seviyesinde bir değişken olarak ASGI çağrılabilir bileşenini dışa açar.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_project.settings')

application = get_asgi_application()