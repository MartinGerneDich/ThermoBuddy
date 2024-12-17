from setuptools import find_packages, setup

package_name = 'my_project'

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
    maintainer='smarty',
    maintainer_email='smarty@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'talker = my_project.my_publisher:main',
            'listener = my_project.my_subscriber:main',
            'temperature_listener = my_project.temperature_listener:main',
            'computation_node = my_project.temperature_computation:main',
            'led_control_node = my_project.temperature_led_control:main',
        ],
    },
)
