from setuptools import setup, find_packages
setup(name="rfid-clone", version="2.0.0", author="bad-antics", description="RFID/NFC cloning and access control research", packages=find_packages(where="src"), package_dir={"":"src"}, python_requires=">=3.8")
