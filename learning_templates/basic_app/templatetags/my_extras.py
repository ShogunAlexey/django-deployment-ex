from django import templates

register = template.library()

@register.filter(name='cut')
def cut(value, arg):
    ''' this cuts out all values of 'arg' from string '''
    return value.replace(arg,'')

# register.filter('cut',cut)
