from libqtile.config import Screen
from libqtile.bar import Bar
from libqtile.widget import *

from themes import Fonts, Colors
from functions import Functions
from ipaddress import IPAddress

class WidgetsList:
	def init_widget_list(self):
		color = Colors()
		font = Fonts()

		wl = [
			GroupBox(
				active = color.light_blue,						# Active group font color
				block_highlight_text_color = color.white,		# Selected group font color
				disable_drag = True,
				font = font.normal,
				fontshadow = font.fontshadow,
				fontsize = font.fontsize,
				highlight_method = 'block',
				inactive = color.light_grey,					# Inactive group font color
				margin_x = 0,
				padding = 6,
				rounded = False,
				this_current_screen_border = color.red,			# Selected group background
				use_mouse_wheel = False,
			),
			CurrentLayoutIcon(
				scale = 0.6,
				padding = 10,
				custom_icon_paths = ['~/.config/qtile/icons/']
			),
			Spacer(),
			WidgetBox(	
				font = font.normal,
				fontsize = font.fontsize,
				foreground = color.light_blue,
				text_closed = "CPU",
				text_open = "CPU",
				widgets = [
					CPUGraph(
						border_color = color.light_grey,
						border_width = 1,
						core = 'all',
						fill_color = color.red,
						graph_color = color.red,
						line_width = 2,
						margin_x = 6,
						margin_y = 3,
						type = 'box',
					)
				]
			),			
			CPU(	
				font = font.normal,
				fontsize = font.fontsize,
				padding = 6,
				format = "{load_percent}%"
			),
			Spacer(	
				length = 20,
			),
			WidgetBox(	
				font = font.normal,
				fontsize = font.fontsize,
				foreground = color.light_blue,
				text_closed = "MEM",
				text_open = "MEM",
				widgets = [
					MemoryGraph(
						border_color = color.light_grey,
						border_width = 1,
						fill_color = color.red,
						graph_color = color.red,
						line_width = 2,
						margin_x = 6,
						margin_y = 3,
						type = 'box',
					)
				]
			),			
			Memory(	
				font = font.normal,
				fontsize = font.fontsize,
				padding = 6,
				format = "{MemPercent}%"
			),
			Spacer(	
				length = 20,
			),
			WidgetBox(	
				font = font.normal,
				fontsize = font.fontsize,
				foreground = color.light_blue,
				text_closed = "NET",
				text_open = "NET",
				widgets = [
					Net(
					font = font.normal,
					fontsize = font.fontsize,
					padding = 4,
					format = "{down}",
					interface = "enp2s0",
					)
				]
			),
			IPAddress(	
				font = font.normal,
				fontsize = font.fontsize,
				padding = 6,
				interface = "enp2s0",
			),
			Spacer(	
				length = 20,
			),
			WidgetBox(	
				font = font.normal,
				fontsize = font.fontsize,
				foreground = color.light_blue,
				text_closed = "VOL",
				text_open = "VOL",		
			),
			Volume(	
				font = font.normal,
				fontsize = font.fontsize,
				padding = 4,
				step = 5,
			),
			Spacer(	
				length = 10,
			),
			Clock(
				font = font.normal,
				fontsize = font.fontsize,
				foreground = color.white,
				format = '%H:%M:%S',
				padding = 10,
			),
		]
		return wl


class Bars:
	widget_list = WidgetsList()
	color = Colors()

	def init_top_bar(self):
		return Bar(
			widgets = self.widget_list.init_widget_list(),
			opacity = 1.0,
			size = 26,
			background = self.color.grey,
		)


class Screens:
	bar = Bars()
	
	def init_single_screen(self):
		return [
			Screen(
				top = self.bar.init_top_bar()
			)
		]