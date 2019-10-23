from django.conf.urls import url, include
from django.contrib import admin
from django.urls import re_path, path
from graphene_django.views import GraphQLView

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    re_path(r'^graphql$', GraphQLView.as_view(graphiql=True)),
]