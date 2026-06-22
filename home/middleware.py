import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user if hasattr(request, 'user') else None
        username = user.username if user and user.is_authenticated else 'anonymous'
        timestamp = datetime.now().strftime('%d/%b/%Y %H:%M:%S')

        logger.info(
            '[%s] [%s] "%s %s" %s — user: %s',
            timestamp,
            request.META.get('REMOTE_ADDR'),
            request.method,
            request.get_full_path(),
            response.status_code,
            username,
        )

        return response