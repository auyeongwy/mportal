A website portal named mportal running on fast CGI. Programmed in Python, it is deployed on apache httpd via mod_wsgi. It accepts secure connections. A user can login via secure authentication verified via a database (in this case integration to Postgresql via psycop2). It deploys session cookies and re-directions for moving the user to secure pages. Templating engine wheezy.template is used to render web pages.

This software is developed on my free time as a proof-of-concept for my own curiosity. Not suitable for production use out of the box since it is a tech demo for myself. You won't expect any warranty or much support. I will update it when I feel compelled to, though I always try to only commit bug-free versions.

There is an imperfection with secure authentication/connection where a secure connection is based off user's session cookie. I don't feel inclined to resolve it as it may not matter for certain applications.

The content of this software - "mportal" is licensed under the Apache License, Version 2.0 as follows:

===========================================================================
Copyright 2014 Au Yeong Wing Yau

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==========================================================================
