from django.contrib.auth import get_user_model

User = get_user_model()

def route_to_admin(workitem):
    '''route to admin
    this push application is a sample,
    the built-in push application "route_to_superuser"
    should be used instead
    '''
    return User.objects.get(username='admin')
