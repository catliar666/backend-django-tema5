from django.db import models
from mongoengine import Document, StringField, IntField, ObjectIdField
from bson import ObjectId

# Create your models here.
class Personajes(Document):
    id = ObjectIdField(default=ObjectId, primary_key=True)  # Mapea "Id" de MongoDB a "id"
    nombre = StringField(max_length=100, db_field="Nombre")
    tipo_de_monstruo = StringField(max_length=100, db_field="TipoDeMonstruo")
    fecha_de_lanzamiento = StringField(max_length=5, db_field="FechaDeLanzamiento")
    ciudad_natal = StringField(max_length=100, db_field="CiudadNatal")
    edad = IntField(db_field="Edad")
    foto = StringField(db_field="Foto")

    meta = {"collection": "personajes"} 
    
    
class Usuarios(Document):
    id = ObjectIdField(default=ObjectId, primary_key=True)  # Mapea "Id" de MongoDB a "id"
    usuario = StringField(max_length=100, db_field="usuario")
    email = StringField(max_length=100, db_field="email")
    password = StringField(max_length=5, db_field="password")

    meta = {"collection": "usuarios"}



