from django.shortcuts import redirect, render
from .models import Person


def add_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        person = Person(name=name, age=age)
        person.save()
        return render(request, 'personapp/thanks.html')
    else:
        return render(request, 'personapp/add_person.html')


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'personapp/person_list.html', {'persons': persons})


def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('person_list')
