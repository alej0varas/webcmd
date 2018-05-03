import os
import subprocess

from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.contrib import messages


def webcmd(request):
    data = {}
    data["messages"] = []
    if request.method == 'POST':
        cmd_str = request.POST['cmd']
        home = os.path.expanduser('~')
        cmd_str = cmd_str.replace('~', home)
        if cmd_str:
            if "'" in cmd_str:
                start_sub_str = cmd_str.index("'")
                end_sub_str = cmd_str.index("'", start_sub_str + 1) + 1
                sub_str = [cmd_str[start_sub_str:end_sub_str].strip("'") + "\n"]
                cmd = cmd_str[:start_sub_str].split() + sub_str + cmd_str[end_sub_str:].split()
            else:
                cmd = cmd_str.split()
            try:
                p = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, )
                data['stdout'], data['stderr'] = p.communicate()
                data['stdout'] = data['stdout'].split('\n')
                data['stderr'] = data['stderr'].split('\n')
            except OSError:
                data["messages"].append("Comando no existe. %s" % cmd)
    # select mod, aka template name
    mod = request.POST.get('mod', '')
    template_name = mod + 'webcmd.html'
    data['mod'] = mod

    return render_to_response(
        template_name,
        data, )
        
