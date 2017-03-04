from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tienda

#para django 1.10
from django.utils.deprecation import MiddlewareMixin


class SubdomainTiendaMiddleware(MiddlewareMixin):
	def process_request(self, request):
		host_parts = request.get_host().split('.')
		if len(host_parts) > 2 and host_parts[0] != "www":
			tienda = get_object_or_404(Tienda, slug=host_parts[0])
			# tienda_url = reverse('detail', args=[tienda.slug])
			# url = '{}://{}{}'.format(request.scheme, '.'.join(host_parts[1:]), tienda_url)
			# return redirect(url)
			return render(request, 'main/detail.html',{'object':tienda})
