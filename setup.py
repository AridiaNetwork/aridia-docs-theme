from setuptools import setup
import aridia_docs_theme

setup(
    name='aridia-docs-theme',
    version=aridia_docs_theme.__version__,
    description='Theme for AridiaCraft',
    url='https://github.com/AridiaNetwork/aridia-docs-theme',
    author='AridiaNetwork',
    license='MIT',

    packages=['aridia_docs_theme'],
    install_requires=['sphinx_rtd_theme==0.1.9'],

    message_extractors={
        'src/theme/js': [
            ('**.js', 'javascript', None),
        ]
    },

    zip_safe=False,
    package_data={'aridia_docs_theme': [
        '*.json',
        'favicon.ico',
        'theme.pot',
        'templates/*.html',
        'static/*',
        'static/*/*',
        'extra/*'
    ]},
    scripts=[
        'dist/scripts/build-language',
        'dist/scripts/language-code',
        'dist/scripts/list-translations',
        'dist/scripts/list-versions',
        'dist/scripts/pr-comment',
        'dist/scripts/pr-deploy',
        'dist/scripts/travis-prepare'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
    ]
)
