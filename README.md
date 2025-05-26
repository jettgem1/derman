# Derman Frankincense Website

A professional website for Derman Frankincense, showcasing premium Boswellia species from Northern Somalia. Built with Django and deployed on Vercel.

## About

This website serves as the digital presence for Derman Frankincense, featuring:
- Company information and mission
- Product details and specifications
- Contact information
- Global market presence

## Technology Stack

- **Framework**: Django
- **Deployment**: Vercel
- **Frontend**: Bootstrap 5
- **Styling**: Custom CSS
- **Icons**: Font Awesome

## Features

- Responsive design
- Mobile-friendly layout
- Static file optimization
- SEO-friendly structure

## Local Development

1. Clone the repository:
```bash
git clone [repository-url]
cd derman
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python manage.py runserver
```

## Deployment on Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

For production deployment:
```bash
vercel --prod
```

## Environment Variables

Create a `.env` file in the root directory with:
```
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=.vercel.app
```

## Static Files

Collect static files before deployment:
```bash
python manage.py collectstatic --noinput
```
