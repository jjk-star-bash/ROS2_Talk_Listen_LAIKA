from setuptools import find_packages, setup

package_name = 'talk_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joshkraus',
    maintainer_email='jjk226@lehigh.edu',
    description='Simple test demonstration for project LAIKA',
    license='APACHE 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello_laika = talk_pkg.hello_world:main",
            "listen_laika = talk_pkg.hello_listener:main"
        ],
    },
)
