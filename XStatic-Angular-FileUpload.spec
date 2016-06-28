#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-FileUpload
Version  : 1.4.0.1
Release  : 5
URL      : https://pypi.python.org/packages/source/X/XStatic-Angular-FileUpload/XStatic-Angular-FileUpload-1.4.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Angular-FileUpload/XStatic-Angular-FileUpload-1.4.0.1.tar.gz
Summary  : Angular-FileUpload 1.4.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-FileUpload-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Angular-Filepload
-------------------------
Angular-FileUpload JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Angular-FileUpload package.
Group: Default
Provides: xstatic-angular-fileupload-python

%description python
python components for the XStatic-Angular-FileUpload package.


%prep
%setup -q -n XStatic-Angular-FileUpload-1.4.0.1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
