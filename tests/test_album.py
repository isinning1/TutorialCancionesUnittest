import unittest

from src.logica.coleccion import Coleccion
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session

class AlbumTestCase(unittest.TestCase):
    
    def test_prueba(self):
        self.assertEqual(0, 0)
    
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea los objetos'''
        self.album1 = Album(titulo = 'Corazones', ano = 1990, descripcion = 'No tiene', medio = Medio.CD, canciones = [])
        self.album2 = Album(titulo = 'La voz de los 80s', ano = 1984, descripcion = 'No tiene', medio = Medio.CASETE, canciones = [])
        self.album3 = Album(titulo = 'Pateando piedras', ano = 1986, descripcion = 'No tiene', medio = Medio.DISCO, canciones = [])
        self.album4 = Album(titulo = 'La cultura de la basura', ano = 1987, descripcion = 'No tiene', medio = Medio.DISCO, canciones = [])

        '''Adiciona los objetos a la sesión'''
        self.session.add(self.album1)
        self.session.add(self.album2)
        self.session.add(self.album3)
        self.session.add(self.album4)

        '''Persiste los objetos y cierra la sesión'''
        self.session.commit()
        self.session.close()
    
    def tearDown(self):
        '''Abre la sesión'''
        self.session = Session()

        '''Consulta todos los álbumes'''
        busqueda = self.session.query(Album).all()

        '''Borra todos los álbumes'''
        for album in busqueda:
            self.session.delete(album)

        self.session.commit()
        self.session.close()

    def test_agregar_album(self):
        '''Prueba la adición de un álbum'''
        resultado = self.coleccion.agregar_album(titulo = "Nada personal", anio = 1985, descripcion = "No tiene", medio = Medio.CASETE)
        self.assertEqual(resultado, True)     