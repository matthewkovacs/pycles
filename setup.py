from distutils.core import setup

setup(
    name="PyCLES",
    description="Common language effect size implemented in Python",
    version="0.0",
    packages=["pycles"],
    license="MIT",
    author="Matthew Kovacs",
    url="https://github.com/matthewkovacs/pycles",
    requires = [
        "numpy",
        "scipy"
    ]
)

