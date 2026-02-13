<div align="center">

# &lt;/&gt; DevSearch

**A Django platform for developers to showcase projects & connect with the community**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 📸 Screenshots

| Featured Projects | Login Page |
<p align="center">
  <img src="Screenshot%202026-02-09%20200038.png" alt="Featured Projects" width="800">
</p>

<p align="center">
  <img src="Screenshot%202026-02-09%20200155.png" alt="Login Page" width="800">
</p>
| Browse all projects with vote ratios & CRUD actions | Secure sign-in with register option |

---

## ✨ Features

- 📁 **Project Management** — Add, view, edit, and delete developer projects
- 👍 **Voting System** — Community vote ratio and total vote count per project
- 🔐 **User Authentication** — Register, login, logout with protected routes
- 🔑 **UUID Project IDs** — Each project uses a unique UUID for secure routing
- 📅 **Timestamps** — Creation dates tracked and displayed on every project
- 🛠️ **Admin Panel** — Built-in Django admin interface for full data management

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite (dev) / PostgreSQL (production) |
| Frontend | HTML, CSS, JavaScript |
| Authentication | Django built-in auth system |
| ORM | Django ORM |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/devsearch.git
cd devsearch
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply migrations**
```bash
python manage.py migrate
```

**5. Create a superuser**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

Visit **http://localhost:8000** in your browser 🎉

---

## 📁 Project Structure

```
devsearch/
├── devsearch/          # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/           # Projects app
│   ├── models.py       # Project & Vote models
│   ├── views.py        # CRUD views
│   ├── urls.py
│   └── forms.py
├── users/              # User authentication app
│   ├── models.py
│   ├── views.py
│   └── forms.py
├── templates/          # HTML templates
├── static/             # CSS, JS, and image assets
├── images/             # README screenshots
├── manage.py
└── requirements.txt
```

---

## 🗺️ URL Routes

| Route | Description |
|---|---|
| `/` | Home — Featured projects listing |
| `/login/` | User login |
| `/register/` | New user registration |
| `/add-project/` | Add a new project *(login required)* |
| `/update-project/<id>/` | Edit an existing project *(login required)* |
| `/delete-project/<id>/` | Delete a project *(login required)* |
| `/admin/` | Django admin panel |

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch → `git checkout -b feature/your-feature`
3. Commit your changes → `git commit -m 'Add some feature'`
4. Push to the branch → `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Built with ❤️ using Django &nbsp;·&nbsp; ⭐ Star this repo if you found it helpful!
</div>
