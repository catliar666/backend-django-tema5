import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Personajes
from bson import ObjectId

from django.http import JsonResponse

def todos(request):
    personajes = Personajes.objects.all()
    personajes_list = list(personajes)

    if personajes_list:
        return JsonResponse({
            "mensaje": "Personajes encontrados",
            "personajes": [
                {
                    **p.to_mongo(),
                    "_id": str(p.id)
                }
                for p in personajes_list
            ]
        }, safe=False)
    else:
        return JsonResponse({"error": "No hay personajes en la base de datos"}, status=404)

@csrf_exempt
def create_personaje(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            personaje_id = data.get("id")
            if personaje_id:
                personaje_id = ObjectId(personaje_id)
            
            personaje = Personajes(
                id=personaje_id,
                nombre=data.get("Nombre"),
                tipo_de_monstruo=data.get("TipoDeMonstruo"),
                fecha_de_lanzamiento=data.get("FechaDeLanzamiento"),
                ciudad_natal=data.get("CiudadNatal"),
                edad=data.get("Edad"),
                foto=data.get("Foto")
            ) 
            personaje.save()
            return JsonResponse({"mensaje": "Personaje insertado correctamente", "id": str(personaje.id)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def find_personaje(request, id=None):
    try:
        if id:
            # Buscar por ID
            print(f"Recibido ID: {id}")
            if not ObjectId.is_valid(id):
                return JsonResponse({"error": f"'{id}' no es un ObjectId válido"}, status=400)
            personaje = Personajes.objects.filter(id=ObjectId(id)).first()
            if personaje:
                return JsonResponse({
                    "_id": str(personaje.id),
                    "Nombre": personaje.nombre,
                    "TipoDeMonstruo": personaje.tipo_de_monstruo,
                    "Edad": personaje.edad
                })
            else:
                return JsonResponse({"error": "Personaje no encontrado"}, status=404)

        # Si no se pasa ID, usar filtros dinámicos
        nombre = request.GET.get("nombre")
        tipo = request.GET.get("tipo_de_monstruo")
        edad = request.GET.get("edad")

        filtros = {}
        if nombre:
            filtros["nombre__icontains"] = nombre
        if tipo:
            filtros["tipo_de_monstruo__icontains"] = tipo
        if edad:
            try:
                filtros["edad"] = int(edad)
            except ValueError:
                return JsonResponse({"error": "Edad debe ser un número"}, status=400)

        personajes = Personajes.objects.filter(**filtros)

        if personajes:
            return JsonResponse({
                "personajes": [
                    {
                        "_id": str(p.id),
                        "Nombre": p.nombre,
                        "TipoDeMonstruo": p.tipo_de_monstruo,
                        "Edad": p.edad
                    } for p in personajes
                ]
            }, safe=False)
        else:
            return JsonResponse({"error": "No se encontraron personajes con esos filtros"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)




@csrf_exempt
def update_personaje(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            personaje = Personajes.objects.filter(id=ObjectId(id)).first()

            if personaje:
                personaje.update(
                    nombre=data.get("Nombre", personaje.nombre),
                    tipo_de_monstruo=data.get("TipoDeMonstruo", personaje.tipo_de_monstruo),
                    fecha_de_lanzamiento=data.get("FechaDeLanzamiento", personaje.fecha_de_lanzamiento),
                    ciudad_natal=data.get("CiudadNatal", personaje.ciudad_natal),
                    edad=data.get("Edad", personaje.edad),
                    foto=data.get("Foto", personaje.foto)
                )
                personaje.reload()
                return JsonResponse({"mensaje": "Personaje actualizado", "id": str(personaje.id), "nombre": personaje.nombre})
            else:
                return JsonResponse({"error": "Personaje no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def delete_personaje(request, id):
    if request.method == "DELETE":
        try:
            personaje = Personajes.objects.filter(id=ObjectId(id)).first()
            if personaje:
                personaje.delete()
                return JsonResponse({"mensaje": "Personaje eliminado"})
            else:
                return JsonResponse({"error": "Personaje no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)





