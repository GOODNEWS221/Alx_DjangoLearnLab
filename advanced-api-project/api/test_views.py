from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Login the user once for all authenticated tests
        self.client.login(username='testuser', password='testpass')

        # Create authors and books
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        self.book1 = Book.objects.create(
            title="Book One",
            author=self.author1,
            publication_year=2000
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author=self.author2,
            publication_year=2010
        )

        self.create_url = reverse('book-create')
        self.list_url = reverse('book-list')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # -------------------------
    # CREATE TESTS
    # -------------------------
    def test_create_book_unauthenticated(self):
        """Unauthenticated users should be blocked from creating books"""
        self.client.logout()  # ensure not logged in
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2022
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UN  AUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users should be able to create books"""
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2022
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -------------------------
    # UPDATE TESTS
    # -------------------------
    def test_update_book_authenticated(self):
        data = {"title": "Updated Book Title"}
        response = self.client.patch(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book Title")

    # -------------------------
    # DELETE TESTS
    # -------------------------
    def test_delete_book_authenticated(self):
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    # -------------------------
    # FILTER, SEARCH, ORDER TESTS
    # -------------------------
    def test_search_books_by_author(self):
        url = f"{self.list_url}?search=Author One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [book['title'] for book in response.data]
        self.assertIn("Book One", results)

    def test_filter_books_by_title(self):
        url = f"{self.list_url}?title=Book One"
        response = self.client.get(url)
        self.assertEqual(response.stat)

