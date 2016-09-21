from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crm.forms import CustomerAddForm
from crm.models import Customer

# Create your views here.
class CustomerCreate(CreateView):
	model = Customer
	form_class = CustomerAddForm
	template_name = 'crm/customer_add.html'

	#@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		if self.request.user.has_perm('crm.add_customer'):
			return super(CustomerCreate, self).dispatch(*args, **kwargs)
		return HttpResponseRedirect('/admin/')