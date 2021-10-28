#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zc.lockfile
Version  : 2.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/11/98/f21922d501ab29d62665e7460c94f5ed485fd9d8348c126697947643a881/zc.lockfile-2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/98/f21922d501ab29d62665e7460c94f5ed485fd9d8348c126697947643a881/zc.lockfile-2.0.tar.gz
Summary  : Basic inter-process locks
Group    : Development/Tools
License  : ZPL-2.1
Requires: zc.lockfile-license = %{version}-%{release}
Requires: zc.lockfile-python = %{version}-%{release}
Requires: zc.lockfile-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.testing

%description
Basic inter-process locks
        *************************
        
        The zc.lockfile package provides a basic portable implementation of
        interprocess locks using lock files.  The purpose if not specifically
        to lock files, but to simply provide locks with an implementation
        based on file-locking primitives.  Of course, these locks could be
        used to mediate access to *other* files.  For example, the ZODB file
        storage implementation uses file locks to mediate access to
        file-storage database files.  The database files and lock file files
        are separate files.

%package license
Summary: license components for the zc.lockfile package.
Group: Default

%description license
license components for the zc.lockfile package.


%package python
Summary: python components for the zc.lockfile package.
Group: Default
Requires: zc.lockfile-python3 = %{version}-%{release}

%description python
python components for the zc.lockfile package.


%package python3
Summary: python3 components for the zc.lockfile package.
Group: Default
Requires: python3-core
Provides: pypi(zc.lockfile)
Requires: pypi(setuptools)

%description python3
python3 components for the zc.lockfile package.


%prep
%setup -q -n zc.lockfile-2.0
cd %{_builddir}/zc.lockfile-2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603409333
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zc.lockfile
cp %{_builddir}/zc.lockfile-2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/zc.lockfile/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zc.lockfile/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
