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
Processes the 'environ' parameter from WSGI's 'application' function and decide which page/function should be served in response to the client's HTTP request.

Usage:
        import mportal

        def application(environ, start_response)
                ...(other stuff)...
                output_dic = mportal.process_http(environ)
                html = output_dic['html']
                header_list = output_dic['headers'] # Can be an empty list.
                ...(process as per WSGI process)...
"""

import cgi
import login_mgr, standard_pages, console_page
from mportal_tools import mportal_log, mportal_session

def process_http(environ):
	"""
	Processes the 'environ' parameter from WSGI's 'application' function and decide which page/function should be served in response to the client's HTTP request.

	param environ: From WSGI's 'application' function.
	return HTTPResponse object.
	"""

	# GET handlers
	if environ['REQUEST_METHOD'] == 'GET':
		uid = -1
		if 'HTTP_COOKIE' in environ: 
			uid = mportal_session.check_session(environ['HTTP_COOKIE'])


		# User selected http://<mportal-address>
		if len(environ['PATH_INFO']) == 0:
			if uid == -1:
				return login_mgr.login_page()
			else:
				return standard_pages.redirect_console() # Push user to user console as uid is valid - user has logged in.


		# User selected http://<mportal-address>/<other> but no valid session, go to login page
		if uid == -1:
			return standard_pages.redirect_login()


		else:
			if environ['PATH_INFO'] == '/console': # http://<mportal-address>/console
				return console_page.user_console(uid)


	# POST handlers. In this implementation only handles a login request.
	elif environ['REQUEST_METHOD'] == 'POST':
		post_data = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
		post_data_dic = cgi.parse_qs(post_data)
		if 'request' in post_data_dic:
			if post_data_dic['request'][0] == 'login':
				return login_mgr.do_login(post_data_dic)


	return standard_pages.notfound_page()

