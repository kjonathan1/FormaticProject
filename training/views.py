from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def listSession(request): 
    sessions = Session.objects.all()
    context = {'sessions': sessions}
    return render(request, 'training/list-session.html', context)  #create templates/list-session.html before

def createSession(request): 
    form = SessionForm()
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('list-session')
    context = {'form': form}
    return render(request, 'training/form-session.html', context) 

def updateSession(request, pk):
    session = Session.objects.get(id=pk)
    form = SessionForm(instance=session)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid:
            form.save()
            return redirect('list-session')
    context = { 'form': form }
    return render(request, 'training/form-session.html', context)

def showSession(request, pk):
    session = Session.objects.get(id=pk)
    context = { 'session': session }
    return render(request, 'training/show-session.html', context)

def deleteSession(request, pk):
    session = Session.objects.get(id=pk)
    session.delete()
    return redirect('list-session')

#---------------------------------------------------------------------------
# Create your views here.
def listModule(request): 
    modules = Module.objects.all()
    context = {'modules': modules}
    return render(request, 'training/list-module.html', context)  #create templates/list-module.html before

def createModule(request): 
    form = ModuleForm()
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('list-module')
    context = {'form': form}
    return render(request, 'training/form-module.html', context) 

def updateModule(request, pk):
    module = Module.objects.get(id=pk)
    form = ModuleForm(instance=module)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid:
            form.save()
            return redirect('list-module')
    context = { 'form': form }
    return render(request, 'training/form-module.html', context)

def showModule(request, pk):
    module = Module.objects.get(id=pk)
    context = { 'module': module }
    return render(request, 'training/show-module.html', context)

def deleteModule(request, pk):
    module = Module.objects.get(id=pk)
    module.delete()
    return redirect('list-module')

#---------- INSCRIPTION ------------------
def listInscription(request): 
    inscriptions = Inscription.objects.all()
    context = {'inscriptions': inscriptions}
    return render(request, 'training/list-inscription.html', context) 

def createInscription(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    form = InscriptionForm()
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('list-inscription')
    context = {'form': form, 'etudiant_id' : etudiant.id}
    return render(request, 'training/form-inscription.html', context) 

def updateInscription(request, pk):
    module = Module.objects.get(id=pk)
    form = ModuleForm(instance=module)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid:
            form.save()
            return redirect('list-module')
    context = { 'form': form }
    return render(request, 'training/form-module.html', context)

def showInscription(request, pk):
    pass
def deleteInscription(request, pk):
    pass

# ------------- ETUDIANT ---------------
def createEtudiant(request):
    pass

def listEtudiant(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'training/list-etudiant.html', context)  

def updateEtudiant(request, pk):
    pass

def showEtudiant(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    context = { 'etudiant': etudiant }
    return render(request, 'training/show-etudiant.html', context)

def deleteEtudiant(request, pk):
    pass

