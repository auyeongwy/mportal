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

import cgi

def application(environ, start_response):
	"""Implements the WSGI entry function. This just prints out everything in the 'environ' dictionary for degugging and testing."""
	status = '200 OK'
	output = str(environ)
	
	# Check HTTP Request type and print the parameters
	output += '\n\nRequest Method: '
	if environ['REQUEST_METHOD'] == 'GET' and 'QUERY_STRING' in environ:
		output += 'GET\nQuery String: '+environ['QUERY_STRING']

	elif environ['REQUEST_METHOD'] == 'POST':
		post_data_len = 0
		output += 'POST'
		if 'CONTENT_LENGTH' in environ and 'wsgi.input' in environ:
			post_data_len = int(environ['CONTENT_LENGTH'])
			post_data = environ['wsgi.input'].read(post_data_len)
			post_data_dic = cgi.parse_qs(post_data)
			output += '\n'+str(post_data_dic)
		else:
			output += '\nPOST ERROR' 

	else:
		output += '\nPOST ERROR'

	response_headers = [('Content-type', 'text/plain'),('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]
