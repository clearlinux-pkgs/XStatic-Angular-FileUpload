#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-FileUpload
Version  : 12.0.4.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/4d/fd/c3051915d2f12e8fa11f59c01162ce85e38eca15d9ec73a3d7b271b49744/XStatic-Angular-FileUpload-12.0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/fd/c3051915d2f12e8fa11f59c01162ce85e38eca15d9ec73a3d7b271b49744/XStatic-Angular-FileUpload-12.0.4.0.tar.gz
Summary  : Angular-FileUpload 12.0.4 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-FileUpload-python3
Requires: XStatic-Angular-FileUpload-python
BuildRequires : buildreq-distutils3

%description
-------------------------
        
        Angular-FileUpload JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Angular-FileUpload package.
Group: Default
Requires: XStatic-Angular-FileUpload-python3
Provides: xstatic-angular-fileupload-python

%description python
python components for the XStatic-Angular-FileUpload package.


%package python3
Summary: python3 components for the XStatic-Angular-FileUpload package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-Angular-FileUpload package.


%prep
%setup -q -n XStatic-Angular-FileUpload-12.0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533854070
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
