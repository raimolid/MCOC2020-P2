import numpy as np
from barra import Barra

class Reticulado(object):
	"""Define un reticulado"""

	def __init__(self):
		super(Reticulado, self).__init__()

		self.xyz = np.zeros((0,3), dtype=np.double)
		self.Nnodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}

	def agregar_nodo(self, x, y, z=0):
		#Cambiar Tamaño
		self.xyz.resize((self.Nnodos+1,3))
		self.xyz[self.Nnodos,:] = [x,y,z]
		self.Nnodos +=1
		return
		
	def agregar_barra(self, barra):
		#Se agregan las barras a la lista "barras"
		self.barras.append(barra)
		return

	def obtener_coordenada_nodal(self, n): 
		if n >= self.Nnodos:
			return
		return self.xyz[n,:]

	def calcular_peso_total(self):
		peso_total = 0
		for i in self.barras:
			peso_total += i.calcular_peso(self)
		return peso_total

	def obtener_nodos(self):
		xy = []
		for i in range(self.Nnodos):
			xy.append(self.obtener_coordenada_nodal(i))
		return np.array(xy)

	def obtener_barras(self):
		return self.barras
	
	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		"""Implementar"""
		return
	
	def agregar_fuerza(self, nodo, gdl, valor):
		"""Implementar"""
		return
	
	def ensamblar_sistema(self):
		"""Implementar"""
		return
	
	def resolver_sistema(self):
		"""Implementar"""
		return
	
	def recuperar_fuerzas(self):
		"""Implementar"""
		return
	
	def __str__(self):
		s = "nodos:\n"
		for i in range(self.Nnodos):
			s += f"{i} : ( {self.xyz[i][0]}, {self.xyz[i][1]}, {self.xyz[i][2]} )\n"
		s += "barras:\n"
		for j in range(len(self.barras)):
			s += f"{j} : [ {self.barras[j].ni} {self.barras[j].nj} ]\n"
			
		return s
