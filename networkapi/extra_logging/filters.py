# -*- coding:utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from networkapi.extra_logging import local, NO_REQUEST_ID, NO_REQUEST_USER, NO_REQUEST_PATH


class ExtraLoggingFilter(logging.Filter):

    def __init__(self, request=None):
        """Saves *request* (a WSGIRequest object) for later."""
        self.request = request

    def filter(self, record):
        request = self.request

        record.request_id = getattr(request, 'request_id', NO_REQUEST_ID)
        record.request_path = getattr(request, 'request_path', NO_REQUEST_PATH)
        record.request_user = getattr(request, 'request_user', NO_REQUEST_USER)
        return True
