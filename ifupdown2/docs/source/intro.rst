python-ifupdown2
----------------

The python-ifupdown2 package provides the infrastructure for
parsing /etc/network/interfaces file, loading, scheduling, template parsing,
state management and interface dependency generation of interfaces.

It dynamically loads python modules from /usr/share/ifupdownmodules (provided
by the python-ifupdown2-addons package). To remain compatible with other
packages that depend on ifupdown, it also executes scripts under /etc/network/.
To make the transition smoother, a python module under
/usr/share/ifupdownmodules will override a script by the same name under
/etc/network/.

It publishes an interface object which is passed to all loadble python
modules. For more details on adding a addon module, see the section on
adding python modules.

ifupdown2 module calls all modules for every interface declared in the
/etc/network/interfaces file.
