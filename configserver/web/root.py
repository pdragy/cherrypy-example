"""
Root web server
"""

__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import subprocess
import platform
import cherrypy
from datetime import datetime, date, time
from configserver.tools.common import  get_version, render_template, info, error, success, warning

class RootServer:
	@cherrypy.expose
	def index(self, **kwargs):
		sw_version = get_version()
		return render_template("index.html", sw_version = sw_version, current_time = datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), os_info = ', '.join(platform.uname()[:4]), notify_color= subprocess.check_output(["tail", "-n", "1", "indicator_light"]))
