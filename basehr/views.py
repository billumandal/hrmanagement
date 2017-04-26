from django.shortcuts import render

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all().order_by('lastname')
    return render(request, 'basehr/employee_list.html', {'employees':employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee':employee})

def employee_detail_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method = 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_detail_edit.html', {'form':form})