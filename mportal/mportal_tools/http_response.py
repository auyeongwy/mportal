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

class HTTPResponse:
	""" Object that describes a HTTP response to be returned to the client.
	attribute status Describes the HTTP status to be returned. Defaults to '200 OK'. Overwrite if returning a different value.
	attribute headers List of tuples with two values to be returned in the HTTP headers. Default entry within is [('Content-type', 'text/html')]. Change or append as necessary.
	attribute html The html to return to the client.
	"""
	def __init__(self):
		""" Contructor with default values. """
		self.status = '200 OK'
		self.headers = [('Content-type', 'text/html')]
		self.html =''



	def append_content_length(self):
		""" Appends ('Content-Length', <html length>) to HTTPResponse.headers. The value in HTTPResponse.html must of course be populated 
		and finalized before calling this function.
		Usage:
			response = http_respose.HTTPResponse()
			response.html = <some html>
			response.appendContentLength()
			<return response to WSGI>
		"""
		self.headers.append(('Content-Length', str(len(self.html))))
