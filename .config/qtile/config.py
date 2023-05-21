import os
import subprocess

from libqtile import hook

from bindings import Keys, Mouse
from groups import Groups
from layouts import Layouts
from screens import Screens

# TODO
	# Add: Multiple layouts
	# Add: VPN widget
	# Add: Speedtest widget
	# Add: Internet/network/WLAN (availability) widget
	# Add: Battery widget
	# Add: Better theming
	# Modify: IPAddress widget, save external ip locally
	# Modify: autostart.sh
	# Fix: Fullscreen changes window positions

if __name__ in  ['config', '__main__']:

	# Initialize objects
	obj_keys = Keys()
	obj_mouse = Mouse()
	obj_groups = Groups()
	obj_layouts = Layouts()
	obj_screens = Screens()

	# Initialize qtile variables
	keys = obj_keys.init_general_keybindings()
	keys += obj_keys.init_group_keybindings()
	mouse = obj_mouse.init_mouse()
	groups = obj_groups.init_groups()
	layouts = obj_layouts.init_layouts()
	screens = obj_screens.init_single_screen()
	
	# Qtile configuration variables
	auto_fullscreen = True
	bring_front_click = False
	cursor_warp = False
	dgroups_key_binder = None
	dgroups_app_rules = []
	focus_on_window_activation = 'smart'
	follow_mouse_focus = True
	reconfigure_screens = True
	wmname = 'LG3D'
	auto_minimize = True

	
	@hook.subscribe.startup_once
	def start_once():
		home = os.path.expanduser('~')
		subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])