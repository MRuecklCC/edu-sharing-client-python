# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from edu_sharing_client.api.about_api import ABOUTApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from edu_sharing_client.api.about_api import ABOUTApi
from edu_sharing_client.api.adminv1_api import ADMINV1Api
from edu_sharing_client.api.archivev1_api import ARCHIVEV1Api
from edu_sharing_client.api.authenticationv1_api import AUTHENTICATIONV1Api
from edu_sharing_client.api.bulkv1_api import BULKV1Api
from edu_sharing_client.api.clientutilsv1_api import CLIENTUTILSV1Api
from edu_sharing_client.api.collectionv1_api import COLLECTIONV1Api
from edu_sharing_client.api.commentv1_api import COMMENTV1Api
from edu_sharing_client.api.configv1_api import CONFIGV1Api
from edu_sharing_client.api.connectorv1_api import CONNECTORV1Api
from edu_sharing_client.api.iamv1_api import IAMV1Api
from edu_sharing_client.api.knowledgev1_api import KNOWLEDGEV1Api
from edu_sharing_client.api.ltiv13_api import LTIV13Api
from edu_sharing_client.api.mdsv1_api import MDSV1Api
from edu_sharing_client.api.mediacenterv1_api import MEDIACENTERV1Api
from edu_sharing_client.api.networkv1_api import NETWORKV1Api
from edu_sharing_client.api.nodev1_api import NODEV1Api
from edu_sharing_client.api.organizationv1_api import ORGANIZATIONV1Api
from edu_sharing_client.api.ratingv1_api import RATINGV1Api
from edu_sharing_client.api.registerv1_api import REGISTERV1Api
from edu_sharing_client.api.renderingv1_api import RENDERINGV1Api
from edu_sharing_client.api.searchv1_api import SEARCHV1Api
from edu_sharing_client.api.sharingv1_api import SHARINGV1Api
from edu_sharing_client.api.statisticv1_api import STATISTICV1Api
from edu_sharing_client.api.streamv1_api import STREAMV1Api
from edu_sharing_client.api.toolv1_api import TOOLV1Api
from edu_sharing_client.api.trackingv1_api import TRACKINGV1Api
from edu_sharing_client.api.usagev1_api import USAGEV1Api
