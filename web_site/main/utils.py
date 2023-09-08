

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Войти", 'url_name': 'login'},
]
"""{'title': "LOGIN", 'url_name': 'login'},
{'title': "SIGN UP", 'url_name': 'signup'},
{'title': "ADD A GREENHOUSE", 'url_name': 'addgrhs'}"""

class DataMixin:
   def get_data(self, **kwargs):
      context = kwargs
      user_menu = menu.copy()
      if self.request.user.is_authenticated:
         user_menu.pop(0)
         user_menu.pop(0)
         user_menu.pop(0)
      else:
        context['menu'] = user_menu
      return context