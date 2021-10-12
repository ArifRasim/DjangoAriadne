from ariadne.contrib.django.views import GraphQLView
from django.urls import path

from Library.resolver import schema

urlpatterns = [
    path('graphql', GraphQLView.as_view(schema=schema), name='graphql')
]
