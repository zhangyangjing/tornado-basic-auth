from setuptools import setup


classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation',
]

kw = {
    'name':             'tornado-basic-auth',
    'version':          '0.1.1',
    'description':      'basic authentication for tornado',
    'long_description': open('README.rst').read(),
    'author':           'Yangjing Zhang',
    'author_email':     'zhangyangjing@gmail.com',
    'license':          'Apache License 2.0',
    'url':              'https://github.com/zhangyangjing/tornado-basic-auth',
    'keywords':         'tornado digest-auth basic-auth',
    'py_modules':       ['tornado_basic_auth'],
    'classifiers':      classifiers,
    'install_requires': ['tornado>=4.0.0'],
}

if __name__ == '__main__':
    setup(**kw)
