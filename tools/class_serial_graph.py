from matplotlib import pyplot as plt
from matplotlib import animation, style
from serial import Serial
import numpy as np

class liveGraph(animation.FuncAnimation):

	def __init__(self, _interval, label="Pino"):

		style.use('fivethirtyeight')
		self.fig = plt.figure()
		self.ax1 = self.fig.add_subplot(1, 1, 1)
		self.label = label

		self.porta = Serial()
		self.porta.port		= "/dev/ttyUSB0"
		self.porta.timeout	= 5
		self.porta.baudrate	= 9600

		i = 1
		while (not self.porta.is_open and i < 10):

			try:
				self.porta.open()
			except:
				self.porta.port = "/dev/ttyUSB"+str(i)
				i += 1

		self.maior = 1
		self.menor = 0

		self.data_list = [ [0, 0] for i in range(50)]

		super(liveGraph, self).__init__(self.fig, self.animate, interval=_interval)


	def update(self):

		data = self.porta.readline()
		self.porta.flushInput()
		self.data_list.append(data.decode("utf-8").split(","))
	
		if len(self.data_list)>=50:
			self.data_list.pop(0)

	def animate(self,i):
	
		y1 = []
		y2 = [0]
	
		self.update()
		for line in self.data_list:
			y1.append(int(line[0]))
			#y2.append(int(line[1]))
	
		self.ax1.clear()
		
		self.ax1.plot(range(len(y1)), y1, label=self.label, alpha=.5, color='m')
		#ax1.plot(range(len(y2)), y2, label="Pino 3", alpha=.5, color='y')

		self.menor = min(min(y1)*0.8, min(y2)*0.8, self.menor)
		self.maior = max(max(y1)*1.2, max(y2)*1.2, self.maior)
		self.ax1.set_yticks( np.arange(self.menor, self.maior*7/6, (self.maior-self.menor)/6 ) )
		self.ax1.legend()
		self.ax1.grid(True, alpha=.2)
		#plt.savefig("./img/fig"+str(i)+".png")


leitor = liveGraph(100, "A0")
plt.show()
