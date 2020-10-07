from django.test import TestCase
from .models import Term


class TestModel(TestCase):

    def test_correct_term_created(self):
        self.term = Term.objects.create(details = 'test details edited')  
        self.assertEqual(str(self.term),'test details edited')  #test was ok when 'Edited'   ((env) \my_django_app> python manage.py test)        


# pip install pylint-django (Class 'Term' has no 'objects' member)
# ctrl+shift + p --> preferences configure language specific settings --> paste -->
# {
#     "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django"
#     ],

#     "[python]": {

#     }
# }

#  It was before like this 
# {
#     "emmet.showSuggestionsAsSnippets": true,
#     "emmet.triggerExpansionOnTab": true,
#     "files.associations":{"*html":"html"},
#     "emmet.excludeLanguages": [



#         "markdown"
#     ],
#     "emmet.extensionsPath": "",
#     "window.zoomLevel": 0,
#     "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\wsl.exe",
#     "workbench.colorTheme": "Visual Studio Dark"
# }