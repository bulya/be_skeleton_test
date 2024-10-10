import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "be_skeleton_test.settings")

celery_app = Celery("be_skeleton_test")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
