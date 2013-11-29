from django.conf.urls.defaults import url, patterns, include
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView



from rest_framework import viewsets, routers
from rest_framework import permissions

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    model = Group

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',
	url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='bistuoauth/home.html'),
        name='home'
    ),
    # Examples:
    # url(r'^$', 'bistuoauth.views.home', name='home'),
    # url(r'^bistuoauth/', include('bistuoauth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^api/', include(router.urls)),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(
        regex=r'^accounts/login/$',
        view='django.contrib.auth.views.login',
        kwargs={'template_name': 'bistuoauth/login.html'}
    ),
    url(
        regex='^accounts/logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={'next_page': reverse_lazy('home')}
    ),
    url(r'', include('BistuApi.urls')),
)
