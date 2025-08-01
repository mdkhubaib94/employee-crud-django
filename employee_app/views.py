from django.shortcuts import render,redirect,get_object_or_404

from .models import Employee

from .forms import EmployeeForm

# Create your views here.

def index(request):
    return render(request,"employee_app/index.html", {
        "employees" : Employee.objects.all()
    })

  # make sure this import exists

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # after saving, go back to home
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/add.html', {'form': form})



def update_employee(request, id):
    employee = get_object_or_404(Employee, employee_no=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_app/update.html', {'form': form})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, employee_no=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('index')
    return render(request, 'employee_app/delete_confirm.html', {'employee': employee})
