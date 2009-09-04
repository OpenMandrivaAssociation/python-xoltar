%define oname    xoltar
%define name     python-%{oname}
%define version 0.20010601
%define oversion 01jun01
%define release %mkrel 7
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
BuildArch:     noarch

%description
The Xoltar Toolkit is a collection of useful utilities for programming
in Python. Aside from the threadpool module, the toolkit is mostly
concerned with enabling a functional programming style in Python.

%prep
%setup -c %dname
sed -i -e"s/__version__ ==/__version__ =/" threadpool.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -d $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages/
for module in %{modules}; do
  python -c "import $module"
  install -m644 $module.py* $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *_changes.txt
%{_libdir}/python*/site-packages/*.py*

