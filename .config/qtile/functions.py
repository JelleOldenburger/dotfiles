import subprocess as sp

from libqtile import qtile
from libqtile.command import lazy

class Functions:

	#### GROUP FUNCTIONS ####
	
	@staticmethod
	def group_window_movement(idx, switch_group, move_window):
		@lazy.function
		def __inner(qtile):
			# To prevent 'referenced before assignment' error
			index = idx
			
			# Available groups are defined in groups.py
			available_groups = qtile.config.groups
			
			current_group_count = len(qtile.cmd_groups())
			
			current_window = qtile.current_window

			if index is None:
				index = current_group_count

			if index <= current_group_count:			
				if switch_group and not move_window:
					if index == current_group_count:
						qtile.cmd_addgroup(available_groups[index].name)
					qtile.groups[index].cmd_toscreen()
				
				if move_window and current_window is not None:
					if index == current_group_count:
						qtile.cmd_addgroup(available_groups[index].name)
					qtile.current_window.togroup(available_groups[index].name)
					if switch_group:
						qtile.groups[index].cmd_toscreen(toggle=False)
		return __inner
	
	@staticmethod
	def delete_last_group():
		"""Delete the last group if it's empty"""
		@lazy.function
		def __inner(qtile):
			if len(qtile.groups) > 1 and qtile.groups[-1].windows == []:
				if qtile.current_group == qtile.groups[-1]:
					qtile.groups[-2].cmd_toscreen()
				qtile.current_screen.previous_group = None
				qtile.delete_group(qtile.groups[-1].name)
		return __inner
	
	@staticmethod
	def last_group_window_to_previous_group():
		"""Delete the last group if it's empty"""
		@lazy.function
		def __inner(qtile):
			if len(qtile.groups) > 1 and qtile.current_group == qtile.groups[-1]:
				if qtile.current_window:
					qtile.current_window.togroup(qtile.groups[-2].name)
				qtile.groups[-2].cmd_toscreen()
				if qtile.groups[-1].windows == []:
					qtile.current_screen.previous_group = None
					qtile.delete_group(qtile.groups[-1].name)
		return __inner

	
	##### KILL WINDOW FUNCTIONS #####

	@staticmethod
	def kill_all_windows():
		'''Kill all windows in current group'''
		@lazy.function
		def __inner(qtile):
			for window in qtile.current_group.windows:
				window.kill()
		return __inner

	@staticmethod
	def kill_all_windows_minus_current():
		'''Kill all windows in current group, except the current window'''
		@lazy.function
		def __inner(qtile):
			for window in qtile.current_group.windows:
				if window != qtile.current_window:
					window.kill()
		return __inner

	##### DEFAULT LAYOUT #####
	
	@staticmethod
	def default_layout():
		'''Switch to default layout'''
		@lazy.function
		def __inner(qtile):
			current_group = qtile.current_screen.group
			layouts = current_group.layouts
			current_group.cmd_setlayout(layouts[0].name)
		return __inner
	
	#### OTHER ####
	
	def get_internal_ip():
		ifconfig = sp.Popen(['ifconfig', 'enp2s0'], stdout=sp.PIPE)
		grep = sp.Popen(['grep', '-i', 'mask'], stdin=ifconfig.stdout, stdout=sp.PIPE)
		awk = sp.Popen(['awk', '''{print $2}'''], stdin=grep.stdout, stdout=sp.PIPE)
		cut = sp.Popen(['cut', '-f2', '-d:'], stdin=awk.stdout, stdout=sp.PIPE)

		stdout, stderr = cut.communicate()
		output = stdout.decode()
		output = output.replace('\n', '')
		
		return output