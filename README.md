Django Project Templates
=========================
Some project templates to use in Django.

If you want to checkout the different versions then just navigate in the branches.



How to use
----------

Start Project:

    django-admin.py startproject --template=https://github.com/arruda/dj_project_templates/zipball/1.6 --extension="md,py,html"

Start App:

    django-admin.py startapp --template=https://github.com/arruda/dj_project_templates/zipball/app_template


Or add this alias to your .bashrc:

**djproj**

    $ echo "alias djproj='django-admin.py startproject --template=https://github.com/arruda/dj_project_templates/zipball/1.6 --extension=\"md,py,html\"'" >> ~/.bashrc


**djapp**

    $ echo "alias djapp='django-admin.py startapp --template=https://github.com/arruda/dj_project_templates/zipball/app_template'" >> ~/.bashrc


