from rest_framework.response import Response
from rest_framework.views import APIView
import logging
import traceback

logger = logging.getLogger('customLogger')

class UserView(APIView):
    def get(self, request):
        logger.info("Init log from view")
        logger.warning("Init warning from view")
        logger.error("Test error")

        # raise Exception("test raised exception")
        # Uncomment the above line for test the storing of exception traceback in database

        return Response("Success")
