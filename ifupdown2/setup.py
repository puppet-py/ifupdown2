from distutils.core import setup

setup(name='ifupdown2',
      version='0.1',
      description = "ifupdown 2",
      author='Roopa Prabhu',
      author_email='roopa@cumulusnetworks.com',
      url='cumulusnetworks.com',
      packages=['ifupdown'],
      scripts = ['sbin/ifupdown'],
      install_requires = ['python-gvgen'],
      data_files=[('share/man/man8/',
                      ['man/ifup.8', 'man/ifquery.8', 'man/ifreload.8']),
                  ('share/man/man5/',
                      ['man/interfaces.5']),
                  ('/etc/init.d/',
                      ['init.d/networking']),
                  ('/sbin/', ['sbin/ifupdown']),
                  ('/etc/network/ifupdown2/',
                      ['config/ifupdown2.conf']),
                  ('/usr/share/python-ifupdown2/',
                      ['docs/examples/generate_interfaces.py']),
                  ('/usr/share/doc/python-ifupdown2/examples/',
                      ['docs/examples/interfaces',
                       'docs/examples/interfaces_bridge_template_func',
                       'docs/examples/interfaces_with_template']),
                  ('/etc/bash_completion.d/', ['completion/ifup'])]
      )