from django.contrib.auth import get_user_model

User = get_user_model


def get_user_by_username(username):
    """
    Get users based on the username from the database
    """
    if not username:
        return None

    return User.objects.filter(username__iexact=username).first()
