from setuptools import setup, find_packages

setup(
    author="Stiven López",
    description="Paquete para explorar y seleccionar caracteristicas",
    name="incit_meli",
    packages=find_packages(include=["incit", "incit.*"]),
    version="0.1.0"
)
