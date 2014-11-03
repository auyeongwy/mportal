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
Logging module for mportal. The location of the log file is dictated in the file 'mportal.config', which must be placed in the home location defined by the WSGI configuration directive. init_log() will maintain a process-wide file handler to the log file, so it can be called once in the process lifetime and remain valid. close_log() may not be called in the lifetime of a WSGI process since the process ending will just free the resources, but is still included here for completeness.

WSGI may spawn multiple processes, so each process will have an instant of its own file handler writing to the same log file. The process id of each process is included in the logging output to differentiate them.

Usage:
	from mportal_tools import mportal_log
	
	mportal_log.init_log()
	mportal_log.log('Log this string')
	...
	mPOrtal_log.close() # On process exit.
"""

import sys, ConfigParser, os, logging


def init_log():
	"""Initialises the logging mechanism. This will call sys.exit() if there is an I/O error trying to open the log file."""

	# Get logfile name and open it for writing.
	config = ConfigParser.ConfigParser()
	if len(config.read('mportal.config')) == 0:
		sys.exit('Config Error')
	stdout = config.get('LOG', 'logfile')
	if len(stdout) == 0:
		sys.exit('Config Error')

	# Include the process id in logging, since WSGI could spawn multiple processes
	format_str = '[%(asctime)s] ['+str(os.getpid())+'] %(message)s'
	logging.basicConfig(format=format_str,filename=stdout,level=logging.DEBUG)
	logging.debug('Start Logging.')



def log(p_output):
	"""Logs to the log file. This will call sys.exit() if there is an I/O error trying to write to the log file.
	param p_output The string value to log.
	"""
	try:
		logging.debug(p_output)
	except StandardError as e:
		close_log()
		init_log() # Problem writing to logfile, try to rescue. This will call sys.exit() if the problem persists.
		try:
			logging.debug('Logging Redo: '+e.strerror)
			logging.debug(p_output)
		except StandardError as e2:
			sys.exit(e2.strerror) # Persistent problem logging. Call sys.exit()



def close_log():
	"""Closes logging."""
	logging.close()
