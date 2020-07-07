#!/usr/bin/env python3
# import sys
# import numpy as np
# import datetime
# import time


from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np

from package.ui	import plotwindow


class PlotWindow(QWidget, plotwindow.Ui_Form):
	''' GUI window for plotting pressures, etc. '''
	signal_plotter_closed = QtCore.pyqtSignal()

	def __init__(self, chambers, buffer_len, signal_stop_plot):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.chambers = chambers
		self.buffer_len = buffer_len
		self.signal_stop_plot = signal_stop_plot

		colors = (
			(0, 114, 189),
			(216, 83, 25),
			(236, 177, 32),
			(119, 172, 48),
			(0, 0, 0),
			(0, 0, 0),
			(0, 0, 0),
			(0, 0, 0))

		self.lines = dict()
		buffer = [0]*self.buffer_len
		idx = 0
		self.widget_chamberPlot.addLegend()
		for name in self.chambers:
			pen = pg.mkPen(color=colors[idx], width=2)
			self.lines[name] = self.widget_chamberPlot.plot(buffer, buffer, pen=pen, name=name)
			idx = idx + 1
		self.widget_chamberPlot.setLabel('bottom', "<span style=\"font-size:14px\">Time (s)</span>")
		self.widget_chamberPlot.setLabel('left', "<span style=\"font-size:14px\">Gauge Pressure (psi)</span>")
		self.widget_chamberPlot.showGrid(x=True, y=True)
		self.widget_chamberPlot.setYRange(0, 5, update=False)


	def updateDisplay(self, t):
		''' Update plot lines '''
		for name, chamber in self.chambers.items():
			x = self.lines[name].xData
			y = self.lines[name].yData 

			x = np.append(x[1:], t)
			y = np.append(y[1:], chamber['obj'].pres_meas)

			self.lines[name].setData(x,y)


	def clearDisplay(self):
		''' Clear plot lines '''
		buffer = [0]*self.buffer_len
		for line in self.lines.values():
			line.setData(buffer,buffer)


	def closeEvent(self, event):
		''' Clear display and emit signal to stop plotting thread '''
		self.clearDisplay()
		self.signal_stop_plot.emit()
		print('close plotter')
