from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View,CreateView
from .models import Order,Course
from .forms import PersonCreationForm
from django.contrib import messages
def demo(request):
    return render(request,'index.html')

def home(request):
    return render(request,'order.html')
def load_courses(request):
    department_id = request.GET.get('department_id')
    print(department_id )
    courses = Course.objects.filter(department_id=department_id).all()
    print(courses)
    return render(request, 'drop.html', {'courses': courses})

# class EmployeeCreateView(CreateView):
#     model=Order
#     form_class=PersonCreationForm
#     template_name='add.html'
#     success_url=reverse_lazy('add')

# class Orderview(View):
#     def get(self,request,*args,**kwargs):
#         form=PersonCreationForm()
#         return render(request,'add.html',{'form':form})

class Orderview(View):
    def get(self,request,*args,**kwargs):
        form=PersonCreationForm()
        return render(request,'add.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form=PersonCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'order confirmed')
            return render(request,"add.html",{'form':form})
        else:
            return render(request,"add.html",{'form':form})



        # if form.is_valid():
        #     form.save()
           
        #     messages.info(request, 'order confirmed')
        #     return render(request,"add.html",{'form':form})
        # else:
        #     return render(request,"add.html",{'form':form})


# def order_update_view(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     form = PersonCreationForm(instance=order)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('order_change', pk=pk)
#     return render(request, 'add.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department_id')
    print(department_id )
    courses = Course.objects.filter(department_id=department_id).all()
    print(courses)
    return render(request, 'drop.html', {'courses': courses})
    # print(list(courses.values('id','name')))
    # return JsonResponse(list(courses.values('id','name')),safe=False)
