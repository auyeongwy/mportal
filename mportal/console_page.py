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

from mportal_tools import http_response
import template_mgr, mportal_urls

def user_console(p_id):
	""" Returns a user console page.
	return HTTResponse object.
	"""
	response = http_response.HTTPResponse()
	response.html = template_mgr.render_template('console', {'css_url':mportal_urls.get_url('css')})
	return response

