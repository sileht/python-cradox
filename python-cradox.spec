%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name cradox

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes

License:        LGPLv2
URL:            https://github.com/sileht/pycradox
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%description
Python libraries for the Ceph librados library with use cython instead of ctypes


%package -n     python2-%{pypi_name}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  Cython
BuildRequires:  python-jinja2
BuildRequires:  python-pifpaf
BuildRequires:  librados2-devel

Requires:  Cython

%description -n python2-%{pypi_name}
Python libraries for the Ceph librados library with use cython instead of ctypes


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Python libraries for the Ceph librados library with use cython instead of ctypes
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-Cython
BuildRequires:  python3-jinja2
BuildRequires:  python3-pifpaf
BuildRequires:  librados2-devel

Requires:  python3-Cython

%description -n python3-%{pypi_name}
Python libraries for the Ceph librados library with use cython instead of ctypes
%endif


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install


%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitearch}/cradox.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%exclude %{_usrsrc}/debug/*
%exclude %{_libdir}/debug/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/cradox.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Sep 28 2016 Javier Peña <jpena@redhat.com> - 1.3.0-1
- Updated to upstream version 1.3.0

* Mon Aug 1 2016 Javier Peña <jpena@redhat.com> - 1.1.8-3
- Removed gcc from BuildRequires

* Fri Jun 10 2016 jpena <jpena@redhat.com> - 1.1.8-2
- Fixed explicit lib dependencies
- Fixed license and source

* Thu Apr 21 2016 jpena <jpena@redhat.com> - 1.1.8-1
- Initial package.
