# Raju's Portfolio

एक professional Django-based personal portfolio website जो आपकी skills, projects, qualifications और services को showcase करता है।

## Project Features

- **Home Page** - Portfolio का main introduction
- **About Section** - आपके बारे में detailed information
- **Portfolio Gallery** - आपकी projects का showcase
- **Services** - आपकी services की list
- **Qualifications** - Educational और professional qualifications
- **Contact** - Visitors के लिए contact form
- **Responsive Design** - Mobile-friendly layout

## Tech Stack

- **Backend**: Django 4.2.13
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Static Files**: CSS, JavaScript, Images
- **Server**: Gunicorn (Production)

## Installation

### Prerequisites
- Python 3.8+
- pip
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/prajapati-raju/Raju-s-portfolio.git
cd My_portfolio
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# या
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser** (Admin के लिए)
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

Server http://localhost:8000 पर चलेगा

## Project Structure

```
My_portfolio/
├── My_portfolio/          # Main Django project
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── raju_cv/               # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # App URLs
│   ├── admin.py           # Admin configuration
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html
│   ├── about.html
│   ├── portfolio.html
│   ├── services.html
│   ├── qualification.html
│   └── contact.html
├── static/                # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── image/             # Images
│   └── webfonts/          # Font files
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignored files
└── README.md              # This file
```

## Usage

### Admin Panel
Django admin panel को access करने के लिए:
1. `http://localhost:8000/admin` पर जाएं
2. आपके superuser credentials से login करें
3. Content को manage करें

### Adding Content
Admin panel के through portfolio content add कर सकते हैं:
- Projects add करें
- Services update करें
- Qualifications add करें
- Contact messages देखें

## Deployment

### Production Setup

1. **Environment variables set करें** (.env file)
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host/dbname
```

2. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

3. **Run migrations on production**
```bash
python manage.py migrate
```

4. **Start Gunicorn server**
```bash
gunicorn My_portfolio.wsgi:application --bind 0.0.0.0:8000
```

### Recommended Hosting Platforms
- Heroku
- PythonAnywhere
- DigitalOcean
- AWS EC2
- Render

## Contributing

अगर आप इस project को improve करना चाहते हैं:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

यह project personal use के लिए है। अन्य use के लिए contact करें।

## Contact

- **GitHub**: [prajapati-raju](https://github.com/prajapati-raju)
- **Portfolio**: [राजू का पोर्टफोलियो](https://raju-portfolio.example.com)
- **Email**: contact@example.com

## Support

अगर कोई issue या सवाल हो तो GitHub issues पर create करें।

---

**Created with ❤️ by Raju Prajapati**
