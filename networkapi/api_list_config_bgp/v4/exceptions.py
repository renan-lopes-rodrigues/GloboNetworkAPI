# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.exceptions import APIException


class ListConfigBGPNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, msg):
        self.detail = u'ListConfigBGP %s do not exist.' % (msg)


class ListConfigBGPError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, msg):
        self.detail = msg


class ListConfigBGPDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = u'ListConfigBGP does not exists.'


class ListConfigBGPAssociatedToRouteMapEntryException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, list_config_bgp):
        self.detail = u'ListConfigBGP id = {} is associated ' \
                      u'with RouteMapEntries = {}'.\
            format(list_config_bgp.id, list_config_bgp.route_map_entries_id)
