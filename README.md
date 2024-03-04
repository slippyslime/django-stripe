# Test task for Python developer

Start-up instructions:
1. Creating venv
    Create a folder named django-stripe. Clone my project into it using the command: git clone https://github.com/slippyslime/django-stripe.
    Once you have cloned the repository to your server you must create a venv. You should use the following command at the address: django-stripe/
    python3.xx -m venv venv
2. Install requirements
    Navigate to the django-stripe directory using the command: cd django-stripe/
    You should end up at django-stripe/django-stripe/
    Execute the following command: pip install -r requirements.txt
3. Applying migrations
   Create a superuser: Navigate to the djangostripe directory using the following command: cd djangostripe/
   You should be at django-stripe/django-stripe/djangostripe/
   Run the following command: python3.xx manage.py createsuperuser
   Run the following command: python3.xx manage.py migrate
4. Create items through the admin panel
   Start the server: at django-stripe/django-stripe/django-stripe/djangostripe/ run the following command: python3.xx manage.py runserver
   Open a browser and navigate to localhost:8000/admin. Create items using the handy form to do so.
5. Verify that the job is running correctly by going to localhost:8000

