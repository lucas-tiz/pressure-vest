#!/usr/bin/env python3


if __name__ == "__main__":
	import sys
	import yaml
	from PyQt5.QtWidgets import QApplication
	from package import vestapp

	with open('chamber_config.yaml') as f: 
		chamber_config = yaml.load(f, Loader=yaml.FullLoader)

	app = QApplication(sys.argv)
	app.setStyle('Fusion')

	plot = False
	debug_gui = False
	tune = False
	if "plot" in sys.argv[1:]: # option for plotting pressures
		plot = True
	if "debug_gui" in sys.argv[1:]: # option for debugging GUI (no GPIO/peripherals)
		debug_gui = True
	if "tune" in sys.argv[1:]: # option for tuning system/control parameters
		tune = True

	form = vestapp.VestController(chamber_config, plot=plot, debug_gui=debug_gui, tune=tune)
	form.show()
	sys.exit(app.exec_())

