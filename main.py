from p1_limpiar_respuestas.limpiar_respuestas import Limpiar_respuestas
from p2_guardar_datos_BD.guardar_datos import Guardar_datos

class Main_bot:

	def bot(self):
		limpiarRes=Limpiar_respuestas()
		cad=""
		print("""BOT: ¡Hola! 👋 Soy el Asistente Virtual de Almacenes Anfora. 🤖 🍴\n¿Qué deseas? Escribe el numero.\n1. Sucursales(Horario, telefono y ubicacion) ☎\n2. Tienda en linea 🛒\n3. Cotizaciones 💰\n4. Promociones 🔔\n5. Almacenes Anfora: Antes de visitarnos, te invitamos a conocer las medidas preventivas que tenemos acualmente en nuestras tiendas, solo escribe 6 (Se anexa infografia de COVID - 19)\n""")
		rOpcion=int(input("USUARIO: "))
		if rOpcion==1:			
			cad=cad+"1"
			print("BOT: ¡Escribe el ESTADO del cual nos contactas, por favor!\n")
			rEstado=input("USUARIO: ")
			limEstado=limpiarRes.cortar_estado(rEstado)
			print("""BOT: ¡Estas son las sucursales cercanas a ti!\n - San Lorenzo\n🏨 Alfredo del marzo No.702\nColonia: San Lorenzo Tepantitlán, Toluca, Estados de México C.P:50010\n🕑 Lunes a Sábafo\n9:30 am a 7:00 pm y Domingo\n10:00 am a 6:00 pm\n722 237 2726\nhttps://goo.gl/maps/8B5Ui5wE7ziR9dJ69\nAlmacenes Anfora Juarez 1\n🏨 Avenida Juarez sur no. 206\nColonia Centro, Toluca, Estado de México C.P:5000\n🕑 Lunes a Sábado. 10:00 am a\n8:00 pm Domingo 10:00 am a 6:00 pm\n📞 722 214 0284\n""")
			#print(cad)
		elif rOpcion==2:			
			cad=cad+"2"
			print("BOT: 1. Quiero comprar\n2. Quiero rastrear mi pedido 🚚\n3. Tengo dudas 🤔\n4. Tengo un problema con mi pedido 💬\n5. Necesito cancelar mi pedido\n")
			rSucCom=int(input("USUARIO: "))
			if rSucCom==1:				
				cad=cad+"1"
				print("BOT: ¡Equipa tu cocina! 🍽\n¿Quieres que mandemos tu pedido a domicilio o prefieres recogerlo a alguna de nuestras sucursales?\nEscribe la direccion o el nombre de la tienda 👇\n")
				rSucCom=input("USUARIO: ")
				limDomicilio=limpiarRes.cortar_direccion(rSucCom)
				print("BOT: Por favor compárteme tu número de teléfono a 10 dígitos\n")
				rTel=input("USUARIO: ")
				limTelefono=limpiarRes.cortar_telefono(rTel)
				print("BOT: Por favor comparteme tu correo electrónico\n")
				rCorr=input("USUARIO: ")
				limCorreo=limpiarRes.cortar_correo(rCorr)
				print("BOT: ¡Perfecto! 👏, Prepárate 📝 \n💡 TIP: Puedes mandar la foto de tu lista con el nombre de cada artículo y cantidad que necesitas (piezas)\n")
				print("BOT: Un agente tomará tu pedido ¿Estás listo? Sí / No \nTambién puedes escribir Menú para ver otras opciones. 🤖\n")
				rPedi=input("USUARIO: ")
				rPed=rPedi.capitalize()
				if rPed=="Sí" or rPed=="Si":
					print("BOT: En seguida te contactaré con un agente de Ventas.\n*Se contacta con el agente en Cedis*\n")
				#print(cad)
			elif rSucCom==2:
				cad=cad+"2"
				print("BOT: Escribe tu Nº de orden para ver el estatus de tu pedido 📈🤔\n")
				print("BOT: O si lo prefieres, escribe OPERADOR para ayudarte en otros temas.\n")
				rOrden=input("USUARIO: ")
				rOrd=rOrden.upper()
				if rOrd!="OPERADOR":
					print("BOT:  Por último, escribe tu fecha de nacimiento, sigue mi ejemplo: 1 de enero de 2019. 🤗\n")
					rNacimiento=input("USUARIO: ")
					limFechaNacimiento=limpiarRes.cortar_nacimiento(rNacimiento)
					print("BOT: Hemos recibido tu fecha de nacimiento, estamos buscando tu pedido 🔎 \n¡Espera un momento!\n")
					print("BOT: Tu pedido ya está listo. 👇\n(Se ingresa guía de seguimiento) \n¡Gracias por utilizar este servicio!")
					cad=cad+"0"
			elif rSucCom==3:				
				cad=cad+"3"
				print("BOT: Escribe tu Nº de orden para ver el estatus de tu pedido 📈🤔\n")
				rNorden=input("USUARIO: ")
				limOrden=limpiarRes.cortar_orden(rNorden)
				# print(rOrd)
				print(cad)
			elif rSucCom==4:				
				cad=cad+"4"
				print("BOT: Escribe tu Nº de orden para ver el estatus de tu pedido 📈🤔\n")
				rNorden=input("USUARIO: ")
				limOrden=limpiarRes.cortar_orden(rNorden)
				# print(rOrd)
				#print(cad)
		elif rOpcion==3:			
			cad=cad+"3"
			print("BOT: En seguida te contactaré con un agente de Ventas (*Se contacta con el agente en Cedis*)")
			#print(cad)
		elif rOpcion==4:
			cad=cad+"4"
			print("BOT: En seguida te contactaré con un agente de Ventas y link a nuestra página https://www.almacenesanfora.com/")
			#print(cad)

		guardar_datos=Guardar_datos()
		if cad=="1":
			realizo="Consultar sucursales"			
			print("Servicio: %s"%realizo,"\nEstado: %s"%limEstado)
			guardar_datos.save_consultar_sucursal(realizo, limEstado)
		elif cad=="21":
			realizo="Realizo pedido"
			print("Servicio: %s"%realizo,"\nDirección o Nombre de la tienda: %s"%limDomicilio,"\nTelefono: %s"%limTelefono,"\nCorreo electrónico:%s"%limCorreo)
			guardar_datos.save_realizar_pedido(realizo, limDomicilio, limTelefono, limCorreo)
		elif cad=="2210": 
			realizo="Rastreo pedido"
			print("Servicio: %s"%realizo,"\nNo. Orden:%s"%rOrden,"\nFecha nacimiento:%s"%limFechaNacimiento)
			guardar_datos.save_rastrear_pedido(realizo, rOrden, limFechaNacimiento)
		elif cad=="220":
			realizo="Rastreo pedido"
			print("Servicio: %s"%realizo,"\nNo. Orden:%s"%rOrden)
			guardar_datos.save_problema_pedido(realizo, rOrden)
		elif cad=="23":
			realizo="Problemas con mi pedido"
			print("Servicio: %s"%realizo,"\nNo. Orden:%s"%limOrden)
			guardar_datos.save_problema_pedido(realizo, limOrden)
		elif cad=="24":
			realizo="Necesito cancelar mi pedido"
			print("Servicio: %s"%realizo,"\nNo. Orden:%s"%limOrden)
			guardar_datos.save_cancelar_pedido(realizo, limOrden)
		elif cad=="3":
			realizo="Cotizaciones"
			print("Servicio: %s"%realizo)	
			guardar_datos.save_cotizacion(realizo)
		elif cad=="4":
			realizo="Promociones"
			print("Servicio: %s"%realizo)	
			guardar_datos.save_promocion(realizo)
mb=Main_bot()
mb.bot()
