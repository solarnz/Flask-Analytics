from setuptools import setup

setup(
    name="Flask-Analytics",
    version="0.1.0",
    license="MIT",
    author="Mihir Singh (@citruspi)",
    author_email="citruspi@riseup.net",
    py_modules=["flask_analytics"],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
      'Flask',
    ]
)

