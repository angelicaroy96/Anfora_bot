from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Limpiar_respuestas:

	def cortar_estado(self, rEstado):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_estado=word_tokenize(rEstado)
		all_stopwords.append('es')
		all_stopwords.append('se')
		all_stopwords.append('contactan')
		all_stopwords.append('al')
		all_stopwords.append('el')
		all_stopwords.append('estado')
		text_tokens=word_tokenize(rEstado)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_estado:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena

	def cortar_direccion(self, rDireccion):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_direccion=word_tokenize(rDireccion)
		all_stopwords.append('es')
		all_stopwords.append('mi')
		all_stopwords.append('la')
		all_stopwords.append('a')
		all_stopwords.append('direccion')
		all_stopwords.append('direcion')
		all_stopwords.append('dirección')
		all_stopwords.append('direcciom')
		all_stopwords.append('domicilo')
		all_stopwords.append('domicilio')
		all_stopwords.append('domicilio')
		text_tokens=word_tokenize(rDireccion)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_direccion:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena

	def cortar_telefono(self, rTelefono):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_telefono=word_tokenize(rTelefono)
		all_stopwords.append('es')
		all_stopwords.append('mi')
		all_stopwords.append('tel')
		all_stopwords.append('tel.')
		all_stopwords.append('telefono')
		all_stopwords.append('Telefono')
		all_stopwords.append('el')
		all_stopwords.append('numero')
		all_stopwords.append('número')
		all_stopwords.append('núm.')
		all_stopwords.append('de')
		text_tokens=word_tokenize(rTelefono)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_telefono:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena
	
	def cortar_correo(self, rCorreo):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_correo=word_tokenize(rCorreo)
		all_stopwords.append('es')
		all_stopwords.append('mi')
		all_stopwords.append('correo')
		all_stopwords.append('electronico')
		all_stopwords.append('electrónico')
		all_stopwords.append('e')
		all_stopwords.append('mail')
		text_tokens=word_tokenize(rCorreo)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_correo:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena
	
	def cortar_orden(self, rOrden):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_orden=word_tokenize(rOrden)
		all_stopwords.append('es')
		all_stopwords.append('mi')
		all_stopwords.append('numero')
		all_stopwords.append('orden')
		all_stopwords.append('el')
		all_stopwords.append('la')
		all_stopwords.append('numero')
		all_stopwords.append('núm.')
		all_stopwords.append('de')
		text_tokens=word_tokenize(rOrden)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_orden:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena
	
	def cortar_nacimiento(self, rNacimiento):
		stop_words=set(stopwords.words('spanish'))
		all_stopwords=stopwords.words('spanish')
		cl_nacimiento=word_tokenize(rNacimiento)
		all_stopwords.append('es')
		all_stopwords.append('mi')
		all_stopwords.append('fecha')
		all_stopwords.append('nacimineto')
		all_stopwords.append('nacimiento')
		all_stopwords.append('la')
		text_tokens=word_tokenize(rNacimiento)
		tokens_without_sw=[word for word in text_tokens if not word in all_stopwords]
		nueva_oracion=[]
		for w in cl_nacimiento:
			if w not in stop_words:
				nueva_oracion.append(w)
		cadena=" ".join(tokens_without_sw)
		return cadena
