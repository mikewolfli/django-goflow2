from setuptools import setup

setup(
    name='django-goflow',
    version='1.0',
    description='Fork from Eric Simorre\'s django-goflow, updated for modern Python and Django 4/5/6',
    author='Mike Li',
    author_email='mikewolfli@163.com',
    url='***',
    packages=['goflow', 'goflow.apptools', 'goflow.runtime', 'goflow.graphics', 'goflow.graphics2', 'goflow.workflow', 'goflow.apptools.templatetags', 'goflow.runtime.templatetags', 'goflow.workflow.templatetags', 'goflow.graphics2.templatetags'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 6.0',
    ],
    python_requires='>=3.9',
    install_requires=[
        'Django>=4.2,<7.0',
        'django-ninja>=1.5.3',
        'django-ninja-simple-jwt>=0.7.1',
        'Pillow>=10.0.0',
    ],
    include_package_data=True,
    zip_safe=False,
)
