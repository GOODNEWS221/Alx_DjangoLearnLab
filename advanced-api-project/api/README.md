## Book API Endpoints

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/books/` | GET | List all books | ❌ No |
| `/api/books/<int:pk>/` | GET | Retrieve a single book | ❌ No |
| `/api/books/create/` | POST | Create a new book | ✅ Yes |
| `/api/books/<int:pk>/update/` | PUT | Update a book | ✅ Yes |
| `/api/books/<int:pk>/delete/` | DELETE | Delete a book | ✅ Yes |

### Custom Behavior
- `CreateView` and `UpdateView` override `perform_create` and `perform_update` for custom logic.
- Authenticated users only can modify content.