#!/usr/bin/env python3


if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication
	from package import vestapp

	chamber_info = {'aur':{'adc':0, 'pwm':0}, #TODO: put this in main
					'aul':{'adc':1, 'pwm':1},
					'alr':{'adc':2, 'pwm':2},
					'all':{'adc':3, 'pwm':3} }

	app = QApplication(sys.argv)


	plot = False
	debug_gui = False
	if "plot" in sys.argv[1:]:
		plot = True
	if "debug_gui" in sys.argv[1:]:
		debug_gui = True

	form = vestapp.VestController(chamber_info, plot=plot, debug_gui=debug_gui)
	form.show()


	# # plotter
	# from package import plotter
	# plot_window = plotter.PlotWindow()
	# plot_window.show()

	sys.exit(app.exec_())

