from django.shortcuts import render
from .forms import ContactoForm

def inicio(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/inicio.html', {'form': ContactoForm(), 'mensaje': 'Mensaje enviado'})
    else:
        form = ContactoForm()
    return render(request, 'core/inicio.html', {'form': form})
