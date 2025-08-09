from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# GET: List all books (accessible to everyone, with filters/search/order)
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of all books with search, filter, and order support.
    Publicly accessible.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']


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
        serializer.save()  # Optionally: user=self.request.user


# PUT/PATCH: Update a book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<pk>/update/
    Allows authenticated users to update an existing Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
    
    def get_object(self):
        return generics.get_object_or_404(Book, pk=self.kwargs['pk'])


# DELETE: Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


