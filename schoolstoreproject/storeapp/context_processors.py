from department.models import Department
def menu_links(request):
    links=Department.objects.all()
    return dict(links=links)

