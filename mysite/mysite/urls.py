from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime ,hours_ahead , ua_display_good1,display_meta
from books import views
from contact.views import contact 
from contact.views import thanks
from loginpage.views import login
from loginpage.views import index
from loginpage.views import signup
from loginpage.views import registration
from loginpage.views import success
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^uadisplay/$', ua_display_good1),
    url(r'^displaymeta/$', display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$',contact),
    url(r'^contact/thanks/$',thanks),
    url(r'^login/$',login),
    url(r'^index/$',index),
    url(r'^signup/$',signup),
    url(r'^register/$',registration),
    url(r'^success/$',success),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
