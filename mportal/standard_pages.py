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

from mportal_tools import http_response, mportal_log
import template_mgr, mportal_urls


def notfound_page():
	""" Returns a 'page not found'
	return HTTPResponse object.
	""" 
	response = http_response.HTTPResponse()
	response.html = template_mgr.render_template('not_found', {'css_url':mportal_urls.get_url('css')})
	return response



def redirect_console():
	""" Returns a redirection via HTTP headers to redirect user to a user console.
	return HTTPResponse object.
	""" 
	"""The HTML output"""
	response = http_response.HTTPResponse()
	response.status = '303 See Other'
	#response.headers.append(('Location', 'https://127.0.0.1/mportal/console'))
	response.headers.append(('Location', mportal_urls.get_url('console')))
	response.html = template_mgr.render_template('redirect', {})
	#response.html = """<!DOCTYPE html>
	#<html lang="en">
	#<head>
	#<meta charset="UTF-8">
	#</head> 
	#<body>
	#</body>
	#</html>"""

	return response



def redirect_login():
	""" Returns a redirection via HTTP headers to redirect user to the login page.
	return HTTPResponse object.
	""" 
	response = http_response.HTTPResponse()
	response.status = '303 See Other'
	response.headers.append(('Location', mportal_urls.get_url('home')))
	response.html = template_mgr.render_template('redirect', {})
	#response.html = """<!DOCTYPE html>
	#<html lang="en">
	#<head>
	#<meta charset="UTF-8">
	#</head> 
	#<body>
	#</body>
	#</html>"""

	return response


