from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny

from api.models import Quote, Rating
from api.serializers import QuoteSerializer

class QuotePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        if view.action == 'destroy':
            return request.user.is_authenticated and request.user.has_perm('api.delete_quote')
        if view.action == 'retrieve':
            if obj.is_moderated:
                return True
            else:
                return request.user.is_authenticated and request.user.has_perm('api.view_quote')
        if view.action == 'update':
            return request.user.is_authenticated and request.user.has_perm('api.change_quote')
        return True



class QuoteViewSet(viewsets.ModelViewSet):

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [QuotePermission]
    # print(permission_classes)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.has_perm('api.view_non_moderated_quotes'):
            return queryset
        else:
            return queryset.filter(is_moderated=True)


class IncreaseRating(TemplateView):
    template_name = 'webapp/index.html'

    def get(self, request, *args, **kwargs):
        self.quote = Quote.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user

        try:
            rating = Rating.objects.get(quote=self.quote, user=user)
            if rating.rating == -1:
                self.quote.sum_rating += 2
                self.quote.save()
                rating.rating = 1
                rating.save()
            else:
                return HttpResponse({'error': 'error'}, status=400)
        except Rating.DoesNotExist:
            Rating.objects.create(user=user, quote=self.quote, rating=1)
            self.quote.sum_rating += 1
            self.quote.save()

        return HttpResponse(self.quote.sum_rating)


class DecreaseRating(TemplateView):
    template_name = 'webapp/index.html'

    def get(self, request, *args, **kwargs):
        self.quote = Quote.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user

        try:
            rating = Rating.objects.get(quote=self.quote, user=user)
            if rating.rating == 1:
                self.quote.sum_rating -= 2
                self.quote.save()
                rating.rating = -1
                rating.save()
            else:
                return HttpResponse({'error': 'error'}, status=400)
        except Rating.DoesNotExist:
            Rating.objects.create(user=user, quote=self.quote, rating=-1)
            self.quote.sum_rating -= 1
            self.quote.save()

        return HttpResponse(self.quote.sum_rating)


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')