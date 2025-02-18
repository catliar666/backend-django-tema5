from django.db import models
import mongoengine

# Create your models here.
class Personajes(mongoengine.Document):
    id = mongoengine.StringField(primary_key=True)  # Mapea "Id" de MongoDB a "id"
    nombre = mongoengine.StringField(max_length=100, db_field="Nombre")
    tipo_de_monstruo = mongoengine.StringField(max_length=100, db_field="TipoDeMonstruo")
    fecha_de_lanzamiento = mongoengine.StringField(max_length=5, db_field="FechaDeLanzamiento")
    ciudad_natal = mongoengine.StringField(max_length=100, db_field="CiudadNatal")
    edad = mongoengine.IntField(db_field="Edad")
    foto = mongoengine.StringField(db_field="Foto")

    meta = {"collection": "personajes"}  # Asegurar que se usa la colección correcta



