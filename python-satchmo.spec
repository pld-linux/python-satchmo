%define		module	satchmo

Summary:	The web shop for perfectionists with deadlines
Summary(pl.UTF-8):	Sklep WWW dla perfekcjonistów z ograniczeniami czasowymi
Name:		python-satchmo
Version:	0.8.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://satchmoproject.com/snapshots/%{module}-%{version}.tar.gz
# Source0-md5:	3e7f13edfc717d88f754f475182072d6
URL:		http://www.satchmoproject.com/
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 1:0.6-0.c1
BuildRequires:	rpm-pythonprov
Requires:	python-django = 0.96
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Satchmo is a web shop based on Django framework.

%description -l pl.UTF-8
Satchmo to sklep internetowy oparty na szkielecie Django.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

find $RPM_BUILD_ROOT -type f -name '*.pyc' -exec rm "{}" ";"
find $RPM_BUILD_ROOT -type f -name '*.pyo' -exec rm "{}" ";"
find $RPM_BUILD_ROOT -type f -exec sed -i -e "s#$RPM_BUILD_ROOT##g" "{}" ";"

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
# %%py_postclean
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name '*.py' -a -not -path '*_template*' -exec rm "{}" ";"
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -path '*_template*' -a -name '*.py[oc]' -exec rm "{}" ";"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.*
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/Satchmo-*.egg-info
