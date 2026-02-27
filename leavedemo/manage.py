# #!/usr/bin/env python
# from django.core.management import execute_manager
# try:
#     import settings # Assumed to be in the same directory.
# except ImportError:
#     import sys
#     sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#     sys.exit(1)
#
# if __name__ == "__main__":
#     execute_manager(settings)


#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leavedemo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

