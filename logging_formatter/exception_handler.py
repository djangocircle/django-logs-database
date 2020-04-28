from rest_framework.views import exception_handler
import traceback
import logging

logger = logging.getLogger('customLogger')

def handle_exception(exc, context):
    error_response = exception_handler(exc, context)
    logger.error(traceback.format_exc())
    return error_response
