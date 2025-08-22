import logging

logger = logging.getLogger(__name__)

def send_welcome_email(email: str, name: str):
    """
    Mock email function for development
    """
    logger.info(f"Would send welcome email to {name} at {email}")
