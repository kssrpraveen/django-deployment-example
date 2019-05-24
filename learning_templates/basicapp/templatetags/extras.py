from django import template
register=template.Library()
@register.filter(name="cut")
def cut(self,arg):
    return self.replace(arg,' ')