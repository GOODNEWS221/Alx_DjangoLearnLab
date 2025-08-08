from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters



# GET: List all books (accessible to everyone)
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all books (publicly accessible).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# GET: Retrieve a specific book (accessible to everyone)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/
    Retrieves a single book by ID (publicly accessible).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# POST: Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Allows authenticated users to create a new Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()  # Optionally add user=self.request.user


# PUT/PATCH: Update a book (authenticated users only)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering (exact matches)
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching (partial matches)
    search_fields = ['title', 'author']

    # Ordering
    ordering_fields = ['title', 'publication_year']


# DELETE: Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]