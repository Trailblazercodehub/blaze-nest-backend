# Blaze Nest Backend

Blaze Nest is a platform designed to address the housing and entrepreneurial needs of students. It simplifies the lodging search for students and provides a marketplace for student vendors to showcase their products and services.

---

## Features

- Student accommodation search and filtering
- Vendor marketplace for student products and services
- Secure authentication with JWT
- Cloudinary integration for media storage
- RESTful API built with Django REST Framework

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Git](https://git-scm.com/) (optional, for cloning the repository)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/blaze-nest-backend.git
cd blaze-nest-backend
```

### 2. Configure Environment Variables

Create a `.env` file in the project root with the following content (replace with your actual credentials):

```env
DEBUG=True
SECRET_KEY=your-django-secret-key
CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret
```

### 3. Build and Run with Docker Compose

Make sure Docker Desktop is running.

To build and start the services:
```bash
docker compose up -d --build
```

To start the services without rebuilding:
```bash
docker compose up -d
```

---

## API Documentation

Once the server is running, you can access the API documentation (if enabled) at:

- Swagger UI: `http://localhost:8000/swagger/`
- Redoc: `http://localhost:8000/redoc/`

---

## Useful Commands

- **Stop all services:**  
  `docker compose down`

- **View logs:**  
  `docker compose logs -f`

- **Run migrations:**  
  `docker compose exec web python manage.py migrate`

- **Create a superuser:**  
  `docker compose exec web python manage.py createsuperuser`

---

## Project Structure

```
blaze-nest-backend/
├── accommodation/
├── booking/
├── customuser/
├── vendors/
├── maintenance/
├── security/
├── entreprenuership_hub/
├── blazenest/
├── static/
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.