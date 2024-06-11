from django import template

from studentapp.models import CourseMeterial, Teacher

register = template.Library()
@register.simple_tag
def mat_name(course,batch):
    
    material_names = Teacher.objects.get(batches=batch,courses=course)
    return material_names.name

