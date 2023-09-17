# Projects
[Build an expense tracker app in Django](https://www.coursera.org/learn/showcase-build-expense-tracker-app-django/home/week/1)

## How to run
1. Clone the repository
```
git clone https://github.com/kenextra/ManageBookDistribution.git
```
2. Change directory to the `ManageBookDistribution` folder
```
cd ManageBookDistribution
```
3. Create and activate virtual environment
```
python3 -m venv .venv
source env/bin/activate
```
*For windows*
```
python -m venv env
.venv\Scripts\activate
```
4. Install the requirements
```
pip install -r requirements.txt
```
5. Create `.env` file in the current directory and fill your secret variables
```
mv .env.example .env
```
6. Perform database migration
```
python manage.py makemigrations
python manage.py migrate
```
7. Create superuser
```
python manage.py createsuperuser
```
8. Run the server
```
python manage.py runserver
```
9. Open the browser and go to `http://localhost:8000/admin/` to login to the admin panel
10. Go to `Books`` Model in the admin page, click `import` and upload the `BookDistributionExpenses.csv` file in the `data` folder
11. Go to `http://localhost:8000/` to view the application


## Libraries used
- Django
- crispy-bootstrap4
- django-crispy-forms
- django-import-export
- Pillow
- plotly
- python-dotenv

## Acknowledgements
1. [Django Documentation](https://docs.djangoproject.com/en/3.2/)
2. [Create Charts](https://hackmamba.io/blog/2022/03/quickly-create-interactive-charts-in-django/)