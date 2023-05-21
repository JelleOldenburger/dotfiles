import subprocess as sp
from libqtile.widget import base


class InternalIP(base.ThreadPoolText):
	orientations = base.ORIENTATION_HORIZONTAL

	defaults = [
        ("update_interval", 60.0, "Update interval for the InternalIP widget"),
    ]

	def __init__(self, **config):
		super().__init__(**config)
		self.add_defaults(InternalIP.defaults)

	def poll(self):
		ifconfig = sp.Popen(['ifconfig', 'enp2s0'], stdout=sp.PIPE)
		grep = sp.Popen(['grep', '-i', 'mask'], stdin=ifconfig.stdout, stdout=sp.PIPE)
		awk = sp.Popen(['awk', '''{print $2}'''], stdin=grep.stdout, stdout=sp.PIPE)
		cut = sp.Popen(['cut', '-f2', '-d:'], stdin=awk.stdout, stdout=sp.PIPE)

		stdout, stderr = cut.communicate()
		output = stdout.decode()
		output = output.replace('\n', '')
		
		return output


class ExternalIP(base.ThreadPoolText):
	orientations = base.ORIENTATION_HORIZONTAL

	servers = [['curl', 'http://ifconfig.me'],
			   ['curl', 'http://www.icanhazip.com'],
			   ['curl', 'http://ipecho.net/plain'],
			   ['curl', 'http://bot.whatismyipaddress.com'],
			   ['curl', 'https://diagnostic.opendns.com/myip'],
			   ['curl', 'http://checkip.amazonaws.com'],
			   ['curl', 'http://whatismyip.akamai.com'],
			   ['dig', '+short', 'myip.opendns.com', '@resolver1.opendns.com'],
			   ['dig', '+short', 'ANY', 'whoami.akamai.net', '@ns1-1.akamaitech.net'],
			   ['dig', '+short', 'ANY', 'o-o.myaddr.l.google.com', '@ns1.google.com'],
			  ]
	
	count = 0
	
	defaults = [
        ("update_interval", 60.0, "Update interval for the ExternalIP widget"),
    ]

	def __init__(self, **config):
		super().__init__(**config)
		self.add_defaults(ExternalIP.defaults)

	def poll(self):		
		curl = sp.Popen(self.servers[self.count], stdout=sp.PIPE)
		stdout, stderr = curl.communicate()
		output = stdout.decode()
		output = output.replace('\n', '')
		output = output.replace('"', '')
		
		if self.count == len(self.servers) - 1:
			self.count = 0
		else:
			self.count += 1
		return output

	
class IPAddress(base.ThreadPoolText):
	orientations = base.ORIENTATION_HORIZONTAL
	
	count = 0
	
	defaults = [
        ("update_interval", 600.0, "Update interval for the IPAddress widget"),
		("visible", "external", "IP address that is visible by default. external | internal"),
		("interface", None, "Interface to use for getting internal ip address"),
    ]
	
	def __init__(self, **config):
		#super().__init__("", **config)
		base.ThreadPoolText.__init__(self, "", **config)
		self.add_defaults(IPAddress.defaults)
		self.add_callbacks({'Button1': self.set_current})
		

	def	get_internal_ip(self):
		if self.interface:
			ifconfig = sp.Popen(['ifconfig', self.interface], stdout=sp.PIPE)
			grep = sp.Popen(['grep', '-i', 'mask'], stdin=ifconfig.stdout, stdout=sp.PIPE)
			awk = sp.Popen(['awk', '''{print $2}'''], stdin=grep.stdout, stdout=sp.PIPE)
			cut = sp.Popen(['cut', '-f2', '-d:'], stdin=awk.stdout, stdout=sp.PIPE)
			stdout, stderr = cut.communicate()
			output = stdout.decode()
			output = output.replace('\n', '')
			return output
		else:
			return "Interface not set"
	
	def get_external_ip(self):
		servers = [
			['curl', 'http://ifconfig.me'],
			['curl', 'http://ipecho.net/plain'],
			['curl', 'http://checkip.amazonaws.com'],
			['curl', 'http://whatismyip.akamai.com'],
			['dig', '+short', 'ANY', 'whoami.akamai.net', '@ns1-1.akamaitech.net'],
		]
					
		get = sp.Popen(servers[self.count], stdout=sp.PIPE)
			
		stdout, stderr = get.communicate()
		output = stdout.decode()
		output = output.replace('\n', '')
		output = output.replace('"', '')
			
		if self.count == len(servers) - 1:
			self.count = 0
		else:
			self.count += 1
		
		return output
	
	
	def set_current(self):
		if self.visible == 'external':
			self.visible = 'internal'
		else:
			self.visible = 'external'
		self.timer_setup()
	
		
	def poll(self):
		external = self.get_external_ip()
		internal = self.get_internal_ip()
		
		if self.visible == 'external':
			return external
		else:
			return internal

	
	