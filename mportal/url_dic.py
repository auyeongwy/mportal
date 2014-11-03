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

g_url_dic = {'css':'http://127.0.0.1/style.css'} # Dictinary of URLs


def get_url(p_key):
	""" Retrieves URL value. Will return '' if the key does not exist. Idea is that if the calling function does not check, at least a blank value for the URL is written to HTML and the application does not break. 
	
	param p_key URL to retrieve.
	return URL or '' if p_key does not exist.

	usage:
	css_url = url_dic.get_url('css')
	html = '<link rel="stylesheet" type="text/css" href="'+css_url+'">'
	"""
	global g_url_dic
	if p_key in g_url_dic:
		return g_url_dic[p_key]
	else:
		return ''
