
from djcelery import celery
import time


@celery.task 
def add(a, b):
	time.sleep(15)
	return a + b