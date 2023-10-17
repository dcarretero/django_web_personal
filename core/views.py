from django.shortcuts import render, HttpResponse
html_base= """
<h1>Mi web personal</h1>
<ul>
    <li><a href = "/">Portada</a></li>
    <li><a href = "/about-me">Acerca de</a></li>
    <li><a href = "/portfolio">Portfolio</a></li>
    <li><a href = "/contact">Contacto</a></li>
</ul>
"""
# Create your views here.
def home(request):

    return HttpResponse(html_base + """ 
                        <h2>Portada</h2>
                        <p>Esto es la portada</p>
                        """
                        )
def about(request):
    return HttpResponse(html_base + 
                        """
                        <h2>Acerca de</h2>
                        <p>Me llamo Daniel y soy programador</p>
                        """)
    
def portfolio(request):
    return HttpResponse(html_base + 
                        """
                        <h2>Portfolio</h2>
                        <p>Este es el portfolio</p>
                        """)
def contact(request):
    return HttpResponse(html_base + 
                        """
                        <h2>Contacto</h2>
                        <p>Estos son los datos de contacto</p>
                        """)