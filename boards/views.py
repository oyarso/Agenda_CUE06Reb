from django.views.generic import TemplateView 
from django.shortcuts import render 
from django.http import HttpResponse 

class Libro(object): 
    def __init__ (self, titulo, autor, valoracion ): 
        self.titulo=titulo 
        self.autor=autor   
        self.valoracion=valoracion        

class IndexPageView(TemplateView): 
    template_name = "index.html" 
    
def menuView(request): 
    template_name = 'menu.html' 
    return render(request, template_name) 

# def mostrar(request): 
    Libro1= ["Titulo: Django 3 Web Development Cookbook Fourth Edition", "Autor: Aidas Bendoraitis","Valoración: 3250"]   
    Libro2= ["Titulo: Two Scoops of Django 3.x", "Autor: Daniel Feldroy","Valoración: 1570"]   
    Libro3= ["Titulo: Django for Professionals", "Autor: William S. Vincent","Valoración: 2100"] 
    Libro4= ["Titulo: Django for APIs", "Autor: William S. Vincent","Valoración: 2540"]     
    Libro5= ["Titulo: El libro de Django", "Autor: Adian Holovaty"]     
    Libro6= ["Titulo: Python Web Development with Django", "Autor: Jeff Forcier"]     
#     libro = Libro("Juan", "Peréz") 
#     items=[Libro1,Libro2,Libro3,Libro4] 
#     itemsTodos=[Libro1,Libro2,Libro5,Libro6,Libro3,Libro4]   

#     context = {"titulo" : libro.titulo,  "items" : items,"itemsTodos":itemsTodos} 
#     return render(request, "templatesexample.html", context) 

def mostrar(request): 
    libro1 = ["Titulo: Django 3 Web Development Cookbook Fourth Edition", "Autor: Aidas Bendoraitis","Valoración: 3250"]
    libro2 = ["Titulo: Two Scoops of Django 3.x", "Autor: Daniel Feldroy", "Valoración: 1570"]
    
    libro3 = ["Titulo: Django for Professionals", "Autor: William S. Vincent","Valoración: 2100"]
    libro4 = ["Titulo: Django for APIs", "Autor: William S. Vincent", "Valoración: 2540"]

    libro5 = ["Titulo: El libro de Django", "Autor: Adian Holovaty"]
    libro6 = ["Titulo: Python Web Development with Django", "Autor: Jeff Forcier"] 

    items=[libro1,libro2,libro3,libro4] 
    itemsTodos=[libro1,libro2,libro5,libro6,libro3,libro4]  
    context = {"items" : items,"itemsTodos":itemsTodos} 
    return render(request, "templatesexample.html", context) 