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

"""
Manages Login operations.
"""

import os, binascii, Cookie
import standard_pages, console_page, template_mgr, mportal_urls
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
from mportal_tools import mportal_session, http_response, mportal_log


def login_page():
	"""Produces the login page.	Usage: dictionary = login_page.login_page
	return HTTPResponse object.
	"""
	response = http_response.HTTPResponse()
	response.html = template_mgr.render_template('login', {'home_url':mportal_urls.get_url('home'), 'css_url':mportal_urls.get_url('css')})
	return response



def do_login(p_postDataDic):
	""" Attempt a login.
	param p_postDataDic The POST data extracted from HTTP post and organized by cgi.parse_qs.
	return HTTPResponse object
	"""
	uid = mportal_session.login(p_postDataDic)
	if uid != -1:
		response = standard_pages.redirect_console()
		response.headers.append(mportal_session.new_session(uid)); # New session cookie headers
		return response

	else:
		return standard_pages.notfound_page()
