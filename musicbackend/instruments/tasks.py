from celery import shared_task


@shared_task
def add(x, y):
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    return x + y