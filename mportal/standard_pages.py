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

def notfound_page():
	""" Returns a 'page not found'
	return HTTPResponse object.
	""" 
	response = http_response.HTTPResponse()
	response.html = """<!DOCTYPE html>
	<html lang="en">
	<head>
	<title>Title</title>
	<meta charset="UTF-8">
	<meta name="keywords" content="content">
	<link rel="stylesheet" type="text/css" href="http://127.0.0.1/style.css">
	</head> 
	<body>
	<h1>Title</h1>
	<div class="center-block">
	<p class="center-text">Oops page not found.</p>
	</div>
	</body>
	</html>"""

	return response



def redirect_console():
	""" Returns a redirection via HTTP headers to redirect user to a user console.
	return HTTPResponse object.
	""" 
	"""The HTML output"""
	response = http_response.HTTPResponse()
	response.status = '303 See Other'
	response.headers.append(('Location', 'https://127.0.0.1/mportal/console'))
	response.html = """<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	</head> 
	<body>
	</body>
	</html>"""

	return response



def redirect_login():
	""" Returns a redirection via HTTP headers to redirect user to the login page.
	return HTTPResponse object.
	""" 
	response = http_response.HTTPResponse()
	response.status = '303 See Other'
	response.headers.append(('Location', 'https://127.0.0.1/mportal'))
	response.html = """<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	</head> 
	<body>
	</body>
	</html>"""

	return response


