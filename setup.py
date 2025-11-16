cat > setup.py << EOF
from setuptools import setup, find_packages

setup(
    name="spacekit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
)
EOF