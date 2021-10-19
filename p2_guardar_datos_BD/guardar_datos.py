from pymongo import MongoClient
import datetime
from datetime import datetime, date, time, timezone

class Guardar_datos:
	
	
	def save_consultar_sucursal(self, realizo, limEstado):		
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy,
			"estado_sucur":limEstado
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")

	def save_realizar_pedido(self, realizo, limDomicilio, limTelefono, limCorreo):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy,
			"domicilio_nombre__tien":limDomicilio,
			"telefono":limTelefono,
			"correo_electronico":limCorreo
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")
		
	def save_rastrear_pedido(self, realizo,limOrden, limFechaNacimiento):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy,
			"num_orden":limOrden,
			"fecha_nacimiento":limFechaNacimiento
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")


	def save_problema_pedido(self, realizo, limOrden):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy,
			"num_orden":limOrden
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")

	def save_cancelar_pedido(self, realizo, limOrden):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy,
			"num_orden":limOrden
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")

	def save_cotizacion(self, realizo):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")

	def save_promocion(self, realizo):
		client=MongoClient("localhost", 27017)
		db=client['almacen_anfora']
		collection=db['servicio']
		hoy=datetime.now()
		collection.insert_one({
			"nom_serv":realizo,
			"fecha_serv":hoy
			})
		if collection is not None:
			print("Registro Exitoso!!")
		else:
			print("Error al Registrar!!")
