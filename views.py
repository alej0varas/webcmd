import os
import subprocess as s

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.contrib import messages

my_env = {'PATH':os.environ['PATH']}

@login_required
def webcmd(request):
    data = {}
    data["messages"] = []
    cmd = ['/usr/bin/env']

    if request.method == 'POST':
        cmd.extend(request.POST['cmd'].split())
        try:
            p = s.Popen(cmd, stdin=s.PIPE, stdout=s.PIPE, stderr=s.PIPE, env=my_env)
            data['stdout'], data['stderr'] = p.communicate()
        except OSError:
            data["messages"].append("Comando no existe.")


    # select mod, aka template name
    mod = request.POST.get('mod', '')
    template_name = mod + 'webcmd.html'
    data['mod'] = mod

    return render_to_response(template_name,
                              data,
                              context_instance=RequestContext(request))
