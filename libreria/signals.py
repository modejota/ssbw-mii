from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
import logging
logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    logger.info("Usuario %s ha iniciado sesión.", user.username)

@receiver(user_login_failed)
def log_user_login_failed(sender, user=None, **kwargs):
    if user:
        logger.warning("Usuario %s ha fallado al iniciar sesión.", user.username)
    else:
        logger.warning("Usuario desconocido ha fallado al iniciar sesión.")

@receiver(user_logged_out)
def log_user_logout(sender, user=None, **kwargs):
    if user:
        logger.info("Usuario %s ha cerrado sesión.", user.username)
    else:
        logger.warning("Usuario desconocido ha cerrado sesión.")