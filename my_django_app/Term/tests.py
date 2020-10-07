from django.test import TestCase
from .models import Term
from  django.contrib.admin.sites import AdminSite
from .admin import TermModelAdmin

class TestModel(TestCase):

    def test_correct_term_created(self):
        self.term = Term.objects.create(details = 'test details edited')  
        self.assertEqual(str(self.term),'test details edited')  #test was failed when 'test details Edited'  ((env) \my_django_app> python manage.py test)        

class OurRequest(object):
    def __init__(self,user=None):
        self.user = user

class  ModelAdminTest(TestCase):

    def setUp(self):
        self.termsModelAdmin = TermModelAdmin(model = Term,admin_site=AdminSite())

    def test_has_add_permission(self):
        self.assertEqual(self.termsModelAdmin.has_add_permission(OurRequest),False)

    def test_has_delete_permission(self):
        self.assertEqual(self.termsModelAdmin.has_delete_permission(OurRequest), False) #test was failed when ,True  ((env) \my_django_app> python manage.py test)

# Test Coverage
# coverage run --source='Term' manage.py test && coverage report





# for problem # pip install pylint-django (Class 'Term' has no 'objects' member)
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