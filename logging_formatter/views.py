from rest_framework.response import Response
from rest_framework.views import APIView
import logging
import traceback

logger = logging.getLogger('customLogger')

class UserView(APIView):
    def get(self, request):
        try:
            logger.info("Init log from view")
            logger.warning("Init warning from view")
            logger.error("Test error")
        except:
            logger.error(traceback.format_exc())
        
        return Response("Success")
