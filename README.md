Django Project Templates
=========================
Some project templates to use in Django.


How to use
----------

Start Project:

    django-admin.py startproject --template=https://github.com/arruda/dj_project_templates/zipball/1.6/project_template.tar --extension="md,py,html"

Start App:

    django-admin.py startapp --template=https://github.com/arruda/dj_project_templates/zipball/1.6/app_template.tar


Or add this alias to your .bashrc:

**djproj**

    $ echo "alias djproj='django-admin.py startproject --template=https://github.com/arruda/dj_project_templates/zipball/1.6/project_template.tar --extension=\"md,py,html\"'" >> ~/.bashrc


**djapp**

    $ echo "alias djapp='django-admin.py startapp --template=https://github.com/arruda/dj_project_templates/zipball/1.6/app_template.tar'" >> ~/.bashrc


