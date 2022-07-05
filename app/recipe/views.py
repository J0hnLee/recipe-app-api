"""
Views for the recipe APIs.

"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    
    """ViewSet for the Recipe APIs. \n
        You can increase more details in the serializer class.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """Retrive recipes for the current authenticated user only."""
        # return self.queryset.filter(user=self.request.user).order_by('-id')
        return self.queryset.filter(user=self.request.user).order_by('-id')

    # def perform_create(self, serializer):
    #     """Create a new recipe."""
    #     serializer.save(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
