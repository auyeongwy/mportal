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

"""
Template manager using wheezy.template to manage all HTML templates returned by the application. User needs to know how templates are labeled and what input dictionaries are expected. See init_templates() for the templates available. See templates in 'templates' directory to understand how the tempaltes look like and what input values are expected.

usage:
from template_mgr import template_mgr

template_mgr.init_templates()
input_dic = {'home_url':'https://127.0.0.1/home', 'css_url':'http://127.0.0.1/style.css'}
html = render_template('login', input_dic)
"""

from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
from mportal_tools import mportal_log


g_template_dic = {} # Dictionary of prepared templates for rendering.


def init_templates():
	""" Initialize all templates.
	"""
	global g_template_dic
	searchpath = ['mportal/templates']
	engine = Engine(loader=FileLoader(searchpath),extensions=[CoreExtension()])
	
	g_template_dic['login'] = engine.get_template('login.html')
	g_template_dic['console'] = engine.get_template('console.html')
	g_template_dic['not_found'] = engine.get_template('not_found.html')
	g_template_dic['redirect'] = engine.get_template('redirect.html')



def render_template(p_template_label, p_dic):
	""" Generates a HTML web page to be returned to the client.
	param p_template_label What web page to produce. See init_templates() for valid values.
	param p_dic Input dictionary for rendering the web page. See templates in 'template' folder for expected values.
	return HTML as string object.
	"""
	global g_template_dic	
	if p_template_label in g_template_dic:
		return str(g_template_dic[p_template_label].render(p_dic))
	else:
		return 'System error.'

