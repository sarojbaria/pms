from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam
from .forms import ProjectTeamCreationForm,BookCreationForm,TaskASignForm
from .models import City,Books,user_task,Task
from .models import User
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'


class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'


class ProjectTeamCreateView(CreateView):    
    template_name = 'project/create_team.html'
    model = ProjectTeam
    success_url = '/project/list/'
    form_class = ProjectTeamCreationForm
    


from django.shortcuts import render
from .models import Project

def pieChart(request):
    labels = []
    data = []

    user = request.user  # Assuming user is authenticated
    queryset = Project.objects.filter(projectteam__user=user).order_by('-estimated_hours')[:5]

    for proj in queryset:
        labels.append(proj.name)
        data.append(float(proj.estimated_hours))

    return render(request, 'project/pie_chart.html', {
        'labels': labels,
        'data': data
    })



class BookCreateView(CreateView):
    model = Books
    template_name = 'project/create_image.html'
    success_url = '/project/list/'
    form_class = BookCreationForm
        
class BookListView(ListView):
    template_name = 'project/image_list.html'
    model = Books
    context_object_name = 'books'        
  

class TaskASignView(CreateView):
    model = user_task
    template_name = 'project/task_assign.html'
    success_url = '/project/list/'
    form_class = TaskASignForm  
    

class TaskListView(ListView):
    template_name = 'project/task_list.html'
    model = Task
    context_object_name = 'tasks'   

class UpdateStatusView(View):
    
    def post(self, request, pk):
        # Get the task instance
        print("pk....",pk)
        task = Task.objects.get(id=pk)
        print("task....",task)
        
        # Check the current status and update it accordingly
        if task.status == "Not Started":
            task.status = "In Progress"
        elif task.status == "In Progress":
            task.status = "Done"
        
        # Save the updated task
        task.save()
        
        return redirect(reverse('task_list')) #lazy reverse