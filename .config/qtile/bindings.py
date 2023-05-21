import os

from libqtile.config import Key, Drag, Click
from libqtile.command import lazy
from libqtile import bar, hook, qtile

from functions import Functions

# Key aliases
mod = 'mod4'
alt = 'mod1'

# Environment variables
#terminal = os.getenv('TERMINAL')

# TODO:
	# env variables
	# Floating layout keys
	# Keybinding table
	# Grow/shrink window functions

class Keys:
	def init_general_keybindings(self):
		return [
			# GENERAL QTILE FUNCTIONS
			Key([mod, 'control'], 'r', lazy.restart(), desc='Restart qtile'),
			Key([mod, 'control'], 'Delete', lazy.shutdown(), desc='Shutdown qtile'),
			Key([mod, 'control'], 'p', lazy.spawncmd(), desc='Launch prompt'),
			Key([mod, 'control'], 'slash', lazy.hide_show_bar('all'), desc='Hide/show bar'),

			# CHANGE WINDOW FOCUS
			Key([mod], 'Up', lazy.layout.up(), desc='Move focus up'),
			Key([mod], 'Down', lazy.layout.down(), desc='Move focus down'),
			Key([mod], 'Left', lazy.layout.left(), desc='Move focus left'),
			Key([mod], 'Right', lazy.layout.right(), desc='Move focus right'),

			# CHANGE WINDOW POSITION
			Key([mod, 'shift'], 'Up', lazy.layout.shuffle_up(), desc='Move window up'),
			Key([mod, 'shift'], 'Down', lazy.layout.shuffle_down(), desc='Move window down'),
			Key([mod, 'shift'], 'Left', lazy.layout.shuffle_left(), desc='Move window left'),
			Key([mod, 'shift'], 'Right', lazy.layout.shuffle_right(), desc='Move window right'),

			Key([mod, 'shift'], 'Return', lazy.layout.swap_main(), desc='Swap window with main'),

			# CHANGE WINDOW SIZE
			Key([mod, 'control'], 'Right', lazy.layout.grow_main(), desc='Grow main window'),
			Key([mod, 'control'], 'Left', lazy.layout.shrink_main(), desc='Shrink main window'),
			Key([mod, 'control'], 'Up', lazy.layout.grow(), desc=''), # TODO Rewrite function
			Key([mod, 'control'], 'Down', lazy.layout.shrink(), desc=''), # TODO Rewrite function

			Key([mod, 'control'], 'Return', lazy.layout.maximize(), desc='Maximize window'),
			Key([mod, 'control'], 'BackSpace', lazy.layout.reset(), desc='Reset layout'),

			# CHANGE LAYOUT
			Key([mod], "Page_Down", lazy.prev_layout(), desc='Previous layout'),
			Key([mod], "Page_Up", lazy.next_layout(), desc='Next layout'),
			Key([mod], "End", Functions.default_layout(), desc='Default layout'),
			Key([mod], "Home", lazy.layout.flip(), desc='Flip layout'),

			Key([mod], 'f', lazy.window.toggle_fullscreen(), desc='Toggle fullscreen'),

			# LAUNCH PROGRAMS
			Key([mod], 'Return', lazy.spawn('alacritty'), desc='Launch terminal'),
			Key([mod], 'space', lazy.spawn('dmenu_run'), desc='Launch dmenu'),
			Key([mod], 'F2', lazy.spawn('bash /home/jelle/Scripts/dm-config'), desc='Launch dm-config'),

			# KILL PROGRAMS
			Key([mod], 'q',	lazy.window.kill(), desc='Kill window'),
			Key([mod, 'shift'], 'q', Functions.kill_all_windows_minus_current(), desc='Kill all windows minus current'),
			Key([mod, 'control'], 'q', Functions.kill_all_windows(), desc='Kill all windows'),
			Key(['control', 'shift'], 'Escape', lazy.spawn("xkill"), desc='Launch xkill'),

			# GROUP CONTROLS
			Key([mod], "Tab", lazy.screen.prev_group(), desc='Switch to previous group'),
			Key([alt], "Tab", lazy.screen.next_group(), desc='Switch to next group'),

			# VOLUME CONTROL
			Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc='Mute audio'),
			Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-"), desc='Decrease volume'),
			Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+"), desc='Increase volume'),

			# AUDIO CONTROL
			Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='Play/pause audio'),
			Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='Next audio'),
			Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='Previous audio'),

			#### TEST ####
			#Key([mod], 'space', Functions.show_group_info()),
		]


	def init_group_keybindings(self):
		group_keys = ['quoteleft']
		group_keys += [str(i) for i in range(1, 10)]
		group_keys += ['0']

		keys = []

		# QUOTELEFT + NUMBER KEYS FUNCTIONS
		for idx, key in enumerate(group_keys):
			keys.append(Key([mod], key, 
							Functions.group_window_movement(idx, True, False), 
							desc=f'Switch to group {key}'))
			keys.append(Key([mod, 'shift'], key, 
							Functions.group_window_movement(idx, True, True), 
							desc=f'Move window and switch group to {key}'))
			keys.append(Key([mod, 'control'], key, 
							Functions.group_window_movement(idx, False, True), 
							desc=f'Move window to group {key}'))

		# EQUAL KEY FUNCTIONS
		keys.append(Key([mod], 'equal', 
						Functions.group_window_movement(None, True, False), 
						desc='Add group'))
		keys.append(Key([mod, 'shift'], 'equal', 
						Functions.group_window_movement(None, True, True), 
					    desc='Add group, move window and switch group'))
		keys.append(Key([mod, 'control'], 'equal', 
						Functions.group_window_movement(None, False, True), 
						desc='Add group and move window'))

		# MINUS KEY FUNCTIONS
		keys.append(Key([mod], 'minus', 
						Functions.delete_last_group(), 
						desc='Delete last group'))
		keys.append(Key([mod, 'shift'], 'minus', 
						Functions.last_group_window_to_previous_group(), 
						desc='Move window from last group'))
		return keys


class Mouse:
	def init_mouse(self):
		return [
			# MOVE FLOATING WINDOWS
			Drag(
				[mod], 'Button1', lazy.window.set_position_floating(),
				start = lazy.window.get_position()
			),

			# RESIZE FLOATING WINDOW
			Drag(
				[mod], 'Button3', lazy.window.set_size_floating(),
				start = lazy.window.get_size()
			),

			# BRING WINDOW TO FRONT
			Click([mod, alt], 'Button1', lazy.window.bring_to_front())
		]
