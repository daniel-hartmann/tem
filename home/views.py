from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils.encoding import smart_str

from .forms import MailForm

EP_FILENAME = 'Trabalhos Espaciais Manuais - EP - 2015.zip'
EP_FILEPATH = '/Users/daniel/devel/tem/home/static/music/Trabalhos Espaciais Manuais - EP - 2015.zip'
EP_URL = '/static/music/Trabalhos Espaciais Manuais - EP - 2015.zip'

def index(request):
    mailform = MailForm(request.POST or None)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'mailform': mailform,
    })
    
    if request.POST and mailform.is_valid():
        if mailform.save():
            epfile = open(EP_FILEPATH)
            response = HttpResponse(epfile, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(EP_FILENAME)
            return response

    return HttpResponse(template.render(context))

def download(request):
    epfile = open(EP_FILEPATH)
    response = HttpResponse(epfile, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(EP_FILENAME)
    return response