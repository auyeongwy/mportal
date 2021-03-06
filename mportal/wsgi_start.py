# Copyright 2014 Au Yeong Wing Yau
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#!/usr/bin/python
# -*- coding: utf-8 -*-
""" All start-up processes to be called when the WSGI process starts.
"""
from mportal_tools import mportal_log
from mportal_tools import mportal_db
import mportal_urls, template_mgr

mportal_log.init_log() # Initializes logging file handler.
mportal_db.init_db() # Initializes database connections.
mportal_urls.init_urls() # Initializes URL list.
template_mgr.init_templates() # Initializes HTML templates.


