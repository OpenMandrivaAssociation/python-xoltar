%define oname    xoltar
%define name     python-%{oname}
%define version 0.20010601
%define oversion 01jun01
%define release 11
%define dname    %{oname}-toolkit-%{oversion}
%define modules  functional lazy threadpool

Summary:       A collection of utilities for threading and FP in python
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %dname.tar.bz2
License:       LGPL
Group:         Development/Python
BuildRoot:     %{_tmppath}/%{name}-buildroot
Url:           http://www.xoltar.org/languages/python.html
BuildRequires: python
BuildRequires: dos2unix
BuildArch:     noarch

%description
The Xoltar Toolkit is a collection of useful utilities for programming
in Python. Aside from the threadpool module, the toolkit is mostly
concerned with enabling a functional programming style in Python.

%prep
%setup -c %dname
sed -i -e"s/__version__ ==/__version__ =/" threadpool.py

#fix EOLs
dos2unix *.txt

%build

%install
rm -rf %{buildroot}
install -m755 -d %{buildroot}/%{python_sitelib}
for module in %{modules}; do
  python -c "import $module"
  install -m644 $module.py* %{buildroot}/%{python_sitelib}
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *_changes.txt
%{python_sitelib}/*.py


%changelog
* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.20010601-10mdv2011.0
+ Revision: 594264
- install files to python_sitelib dir
- fix doc EOLs

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.20010601-9mdv2011.0
+ Revision: 591442
- python-devel isn't BR here

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.20010601-8mdv2011.0
+ Revision: 590634
- BR python-devel

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.20010601-7mdv2010.0
+ Revision: 431355
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.20010601-6mdv2009.0
+ Revision: 242466
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.20010601-4mdv2008.0
+ Revision: 69370
- use %%mkrel


* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.20010601-3mdk
- Rebuild for new python

* Sat Aug 09 2003 Austin Acton <aacton@yorku.ca> 0.20010601-2mdk
- python 2.3

* Wed Jul 09 2003 Austin Acton <aacton@yorku.ca> 0.20010601-1mdk
- from andi payn <payn@myrealbox.com> :
  - initial specfile

