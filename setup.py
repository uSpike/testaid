import os
import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='testaid',
        version='0.8.5',
        author='RebelCodeBase',
        author_email='rebelcodebase@riseup.net',
        description='Fixtures for ansible, testinfra and molecule',
        long_description='See testaid at github: https://github.com/RebelCodeBase/testaid',
        url='https://github.com/RebelCodeBase/testaid',
        license='Apache-2.0',
        packages=setuptools.find_packages(),
        package_data={
            '': ['*.rst'],
        },
        entry_points={
            'pytest11': ['testaid=testaid.plugin']
        },
        platforms='any',
        zip_safe=False,
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Testing',
            'Topic :: System :: Systems Administration',
            'Framework :: Pytest',

        ],
    )
