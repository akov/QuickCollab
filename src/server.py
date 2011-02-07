'''
Created on Jan 18, 2011

Andrew Kovacs
'''

import web
import sys
import diff_match_patch as dmp_module

urls = ('/', 'server',
        '/download', 'download')

app = web.application(urls, globals())
render = web.template.render('templates/')
my_form = web.form.Form(web.form.Textarea('text_area', id='text_area'))
file_name = ''
cur_text = ''

def run_with_file(a_file_path):
   global cur_text
   global file_name
   f = open(a_file_path, 'r')
   cur_text = f.read()
   file_name = f.name.split('/').pop()
   app.run()
class server(object):
   def __init__(self):
      self.dmp = dmp_module.diff_match_patch()

   def GET(self):
      return render.server(my_form(), cur_text)

   def POST(self):
      global cur_text
      form = my_form()
      form.validates()

      patch_text = form.value['text_patch']
      print cur_text
      patches = self.dmp.patch_fromText(patch_text)
      cur_text = self.dmp.patch_apply(patches, cur_text)[0]
      return cur_text

class download(object):
  def GET(self):
   print file_name
   web.header('Content-Type', 'text/plain')
   web.header('Content-Disposition', 'attachment; filename="' + file_name + '"')
   return cur_text



