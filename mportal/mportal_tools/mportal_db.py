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
""" Provides the database interface to the mportal application. This reads database configuration details from 'mportal.config' in the WSGI-configured working directory. WSGI may spawn multiple processes, so each process will have an instant of its own.

Usage:
from mportal_tools import mportal_db

mportal_db.init_db() # Process-wide initialization.
...
result = mportal_db.login(username,password)
...
"""

import psycopg2
import ConfigParser, sys, re
import mportal_log

g_conn = None # Connection handler to the database.
g_user_pattern = re.compile("^[A-Za-z0-9]+$") # Regular expression compiled pattern for checking variables. Alphanumeric only.


def init_db():
	""" Initializes the database connection process-wide. Will call sys.exit() if an error is encountered. """
	# Parse the config file for database login info.
	config = ConfigParser.ConfigParser()
	if len(config.read('mportal.config')) == 0:
		sys.exit('Config file error')
	db_str = config.get('DATABASE','database')
	user_str = config.get('DATABASE','user')
	password_str = config.get('DATABASE','password')
	host_str = config.get('DATABASE','host')

	# Establish database connection.
	try:
		global g_conn 
		g_conn = psycopg2.connect(database=db_str, user=user_str, password=password_str, host=host_str)
		mportal_log.log("DB connected")
	except psycopg2.Error as e:
		sys.exit('Database connection error')


def close_db():
	""" Closes the DB connection. May never be called from code in a WSGI application. """
	global g_conn
	if g_conn != None:
		g_conn.close()
		g_conn = None



def select_all():
	result = None
	try:
		global g_conn
		cur = g_conn.cursor()
		cur.execute("select members.name, users.password from members inner join users on members.id=users.id;")
		result = cur.fetchall()
		cur.close()
	except psycopg2.Error as e:
		mportal_log.log(e.pgerror)

	return result



def login(p_user, p_digest):
	""" Performs a login check.

	param p_user Username.
	param p_digest Not the actual password, but the processed password digest to compare against in the database.
	return id of user if successful, else -1.
	"""
	# Ensure username is safe.
	#result = False;
	result = -1;
	global g_user_pattern
	if g_user_pattern.match(p_user) is None:
		return result

	# Compare credentials with the database.
	try:
		global g_conn
		cur = g_conn.cursor()
		cur.execute("select * from verify_login2(%s,%s);", [p_user,p_digest])
		data = cur.fetchone()
		if data[0] is not None:
			result = data[0]
		cur.close()
	except psycopg2.Error as e:
		mportal_log.log(e.pgerror)

	return result



def update_session(p_id, p_sessionId):
	""" Updates session id of logged-in user.

	param p_id Id of user to update.
	param p_sessionId Session id to update.
	"""
	try:
		global g_conn
		cur = g_conn.cursor()
		cur.execute("select * from update_session(%s, %s);", [p_id, p_sessionId])
		g_conn.commit()
		cur.close()
	except psycopg2.Error as e:
		mportal_log.log(e.pgerror)



def verify_session(p_sessionId):
	""" Verifies session id of logged-in user.

	param p_sessionId Session id to verify.
	return User id if session id exists. Else false.
	"""
	result = -1
	try:
		global g_conn
		cur = g_conn.cursor()
		cur.execute("select * from verify_session(%s);", [p_sessionId])
		data = cur.fetchone()
		if data[0] is not None:
			result = data[0]
		cur.close()
	except psycopg2.Error as e:
		mportal_log.log(e.pgerror)

	return result
