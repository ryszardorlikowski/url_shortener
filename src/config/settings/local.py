from .base import *
import socket

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
_, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
