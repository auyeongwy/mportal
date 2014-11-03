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


import os, binascii, hashlib, Cookie
import mportal_db 
#import mportal_log


def login(p_post_data_dic):
	""" Process login request. 

	param p_post_data_dic Dictionary returned from WSGI environ['wsgi.input'] and organized by 'cgi.parse_qs'.
	return True or False to indicate login success.
	"""
	if 'user' in p_post_data_dic and 'password' in p_post_data_dic:
		user = p_post_data_dic['user'][0]
		password = p_post_data_dic['password'][0]

		# Relatively naive method to get the digest but sufficient for tech demo.
		pass_hash = hashlib.sha224()
		pass_hash.update(password)
		pass_hash.update(user)
		digest = pass_hash.hexdigest()

		# Login check.
		return mportal_db.login(user,digest)
	else:
		return -1



def new_session(p_id):
	""""
	Generate a session id, prepares the HTTP cookie

	param p_id User id of the user of the session.
	return Formatted HTTP cookie headers for passing back in WSGI response.
	"""
	# Prepares the session cookie.
	session_id = binascii.b2a_hex(os.urandom(8))
	cookie = Cookie.SimpleCookie()
	cookie['mportal'] = session_id
	cookie['mportal']['secure'] = True
	cookie['mportal']['httponly'] = True
	cookie['mportal']['max-age'] = 300 # expires in 5 minutes
	cookie['mportal']['path'] = '/mportal'
	cookie_header = ('Set-Cookie', cookie['mportal'].OutputString())

	# Updates the database.
	mportal_db.update_session(p_id, session_id)
	return cookie_header



def check_session(p_cookie):
	cookie = Cookie.SimpleCookie(p_cookie)
	if 'mportal' in cookie:
		session_id = cookie['mportal'].value
		oid = mportal_db.verify_session(session_id)
		#mportal_log.log('Got session cookie: '+session_id)
		#mportal_log.log('Got id: '+str(oid))
		return oid
	else:
		return -1

