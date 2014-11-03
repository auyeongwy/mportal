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

import os, binascii, Cookie
import standard_pages, console_page
from mportal_tools import mportal_session, http_response


def login_page():
	"""Produces the login page.	Usage: dictionary = login_page.login_page
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
	<p class="center-text">Some Content.</p>
	<table>
	<form action="https://127.0.0.1/mportal" method="post">
	<input type="hidden" name="request" value="login">
	<tr><td style="text-align:right;width:120px;">Username:</td><td><input type="text" name="user" required></td></tr>
	<tr><td style="text-align:right;width:120px;">Password:</td><td><input type="password" name="password" required></td></tr>
	</table>
	<div style="padding:2px;text-align:center;"><input type="submit" value="Submit"></div>
	</form>
	</div>
	</body>
	</html>"""

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
