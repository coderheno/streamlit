[app]

# (str) Title of your application
title = HelloWorldApp

# (str) Package name
package.name = helloworld

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,kiwisolver

# (str) The entry point of your application
entrypoint = main.py

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png
