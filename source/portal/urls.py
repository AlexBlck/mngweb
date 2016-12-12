from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'projects/$',
        views.customer_projects,
        name='customer_projects'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/accept_submission_requirements/$',
        views.project_accept_submission_requirements,
        name='project_accept_submission_requirements'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/$',
        views.project_detail,
        name='project_detail'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/add_collaborator/$',
        views.project_add_collaborator,
        name='project_add_collaborator'),
        url(r'^projects/(?P<project_uuid>[-\w]{36})/remove_collaborator/(?P<contact_uuid>[-\w]{36})/$',
            views.project_remove_collaborator,
            name='project_remove_collaborator'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/ena_details/$',
        views.project_ena_details,
        name='project_ena_details'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/permissions/$',
        views.project_permissions,
        name='project_permissions'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/projectlines/(?P<projectline_uuid>[-\w]{36})/update/$',
        views.projectline_update,
        name='projectline_update'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/download_sample_sheet/$',
        views.download_sample_sheet,
        name='download_sample_sheet'),
    url(r'^projects/(?P<project_uuid>[-\w]{36})/upload_sample_sheet/$',
        views.upload_sample_sheet,
        name='upload_sample_sheet'),
    url(r'^projects/email-link/$',
        views.project_email_link,
        name='project_email_link'),
    url(r'^hostsampletype/typeahead/$',
        views.hostsampletype_typeahead,
        name='hostsampletype_typeahead'),
    url(r'^environmentalsampletype/typeahead/$',
        views.environmentalsampletype_typeahead,
        name='environmentalsampletype_typeahead'),

    # maintain legacy links
    url(r'^customers/(?P<customer_uuid>[-\w]{36})/projects/$',
        views.customer_projects,
        name='legacy_customer_projects'),
]
