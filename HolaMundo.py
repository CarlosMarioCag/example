import math
class test:
	def __init__(self,mensaje):
		self.mensaje=mensaje

	def setMensaje(self, mensaje):
		self.mensaje=mensaje

	def getMensaje(self):
		return self.mensaje

if __name__ == '__main__':
	c1=test("hola mundo")
	print(c1.getMensaje())
	c1.setMensaje("Hola mundo 2")
	print(c1.getMensaje())