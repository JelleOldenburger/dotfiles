from libqtile.bar import Bar
from libqtile.widget import *

from themes import Fonts, Colors

class WidgetsList:

	##### WIDGETS LIST #####

	def init_widget_list(self):
		color = Colors()
		font = Fonts()
		
		wl = []

		wl += [GroupBox(
			active = color.white,							# Active group font colour
			#background = None,
			block_highlight_text_color = color.white,		# Selected group font colour
			#borderwidth = 3,
			#center_aligned = True,
			disable_drag = True,
			#fmt = '{}',
			font = font.normal,
			fontshadow = font.fontshadow,
			fontsize = font.fontsize,
			#foreground = 'ffffff',
			hide_unused = False,							# <------------
			#highlight_color = ['000000', '282828'],		# Selected group highlight color when using 'line' highlight method.
			highlight_method = 'block',						# Selected group method of highlighting: border|block|text|line
			inactive = color.light_grey,					# Inactive group font colour
			#invert_mouse_wheel = False,
			#margin = 3,
			margin_x = 0,	
			#margin_y = None,
			markup = True,									
			#max_chars = 0,
			mouse_callbacks = {},
			#other_current_screen_border = '404040',
			#other_screen_border = '404040',
			padding = 6,
			#padding_x = None,
			#padding_y = None,
			rounded = False,
			spacing = None,
			this_current_screen_border = color.yellow,			# Border or line colour for group on this screen when focused.
			this_screen_border = '215578',
			urgent_alert_method = 'border',
			urgent_border = 'FF0000',
			urgent_text = 'FF0000',
			use_mouse_wheel = False,
			#visible_groups = [],
		)]

		wl += [Spacer()]
		wl += [Clock()]

		return wl


class Bars:

	widget_list = WidgetsList()

	def init_top_bar(self):
		return Bar(
			widgets = self.widget_list.init_widget_list(),
			opacity = 1,
			size = 26,
			background = '#2F343F'
		)
