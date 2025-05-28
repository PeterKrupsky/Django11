import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import MeForm, ProgramForm
from .models import Program_model
from django.db.models import Field
from collections import Counter




def me_form(request):
    form = MeForm()
    print(form)
    return render(request, "me_form.html", {"form": form})

def get(request):
    if request.method == "GET":
        form = MeForm(request.GET)
        if form.is_valid():
            task_value = form.cleaned_data["task"]
            a_value = form.cleaned_data["a"]

            get_obj = Program_model(task=task_value, a=a_value)
            get_obj.save()

            return redirect("one_app:result")
    else:
        form = MeForm()

    return render(request, "form.html", {"form": form})


def program_form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("one_app:result")
    else:
        form = ProgramForm()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "program_form.html", context)

    
def manager_form(request):
    print("Method:", request.method) 
    print("POST data:", request.POST) 
    
    if request.method == "POST":
        form = ProgramForm(request.POST)
        print("Form errors:", form.errors) 
        if form.is_valid():
            form.save()
            return redirect("one_app:result")
    else:
        form = ProgramForm()
    
    return render(request, "manager_form.html", {"form": form})
    


def task(input): 
    retu = ''

    if input == 'Обо мне':
        retu = 'Крупский Пётр Анатольевич'  
    elif input == 'О моей программе':
        retu = 'Управление цепями поставок и бизнес-аналитика'
    elif input == 'О моем руководителе':
        retu = ' Герами Виктория Дарабовна'
    elif input == 'О моем сокурснике':
        retu = 'Владислав Иванов Алексеевич'
    else:
        retu = 'ошибка'
    
    return retu



def result(request):
    object_list = Program_model.objects.all().order_by("-id")
    print("\n\nobject_list: ", object_list)

    task_formulation = object_list.values("task")[0]["task"]
    task_id = object_list.values("id")[0]["id"]
    print("task_id task_formulation: ", task_id, task_formulation)


    values_list = object_list.values_list()[0]
    print("\nvalues_list: ", values_list)
    last_values = [values_list[1], values_list[2]]
    print("\nlast_values:", last_values)


    result = task(last_values[1])
    print("\nresult: ", result)
  
    
    
    update_obj = Program_model.objects.filter(id=task_id)
    update_result = result
    update_obj.update(result = update_result)

    context = {
        "task_formulation": task_formulation,
        "last_values": last_values,
        "result": result,
    }
    return render(request, "result.html", context)


def table(request):
    objects_values = Program_model.objects.values()
    print("\nobjects_values:", objects_values)
    objects_values_list = (
        Program_model.objects.values_list().filter(id__gte=3).order_by("a")
    )  
    print("\nobjects_values_list:", objects_values_list)
    cur_objects = objects_values_list
    statics_val = [
        cur_objects.aggregate(Count("a")),
        cur_objects.aggregate(Min("a")),
        cur_objects.aggregate(Max("a"))

    ]
    print("\nstatics_val:", statics_val)
    statics = {"statics_val": statics_val}
    
    fields = Program_model._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        if isinstance(e, Field):
            verbose_name_list.append(e.verbose_name)
            name_list.append(e.name)
    print("\nverbose_name_list:", verbose_name_list)
    print("\nname_list", name_list)
    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "name_list": name_list,
        "objects_values_list": objects_values_list,
        "verbose_name_list": verbose_name_list,
        "statics": statics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)
