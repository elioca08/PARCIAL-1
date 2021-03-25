from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float

 
engine = create_engine ('sqlite:///eliotech.db')
Session = sessionmaker((engine))
session = Session()

Base = declarative_base()
class programa(Base):
    __tablename__ = 'tabla'
    nombre = Column('nombre', String(50), primary_key = True)
    cant = Column('cant', Integer)
    precio = Column('precio',Float)

print("opciones:\n 1)eliminar\n 2)añadir\n 3)editar\n 4)buscar\n")
n=str(input())
if n == '2':
  h = int(input('cuantos productos deseas añadir: '))
  for x in range(0,h):
    m = input('introducir el producto: ')
    c= input('cantidad de productos en stock:')
    p = input('precio al por menor:')
    add = programa()
    add.nombre = m
    add.cant = c
    add.precio = p
    session.add(add)
    session.commit()
elif n== '1':
    h = input('introducir el nombre del producto a eliminar')
    session.query(programa).filter(programa.nombre == h).delete() 
    session.commit()
elif n == '3':
    op = str(input('desea cambiar: \n a)cantidad \n b) precio \n'))
    h = input('introducir el nombre del producto: ')
    if op == 'a':
        ncant = input('introducir la nueva cantidad en stock: ')
        session.query(programa).filter(programa.nombre == h).update({programa.cant : ncant})
        session.commit()
    if op == 'b':
     o = input('introducir el  nuevo precio: ')
     session.query(programa).filter(programa.nombre == h).update({programa.precio : o})
     session.commit()
elif n== '4':
    k = input('producto que deseas buscar en la base de datos: ')
    producto = session.query(programa).filter(programa.nombre == k).one()
    print("producto:{},cantidad:{},precio:{}".format(producto.nombre, producto.cant, producto.precio))
Base.metadata.create_all(engine)  #== se hace una comparacion : hace una sustitucion
 
