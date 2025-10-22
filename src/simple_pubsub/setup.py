from setuptools import setup

package_name = 'simple_pubsub'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vinoth Kumar',
    maintainer_email='vinoth@example.com',
    description='Simple ROS2 Publisher Subscriber Example',
    license='MIT',
    entry_points={
        'console_scripts': [
            'talker = simple_pubsub.publisher:main',
            'listener = simple_pubsub.subscriber:main',
        ],
    },
)
