%define module nab_markersets

Name:		python-nab-markersets
Version:	0.0.21
Release:	1
Summary:	PEP 508 marker algebra for Python environments
License:	MIT
Group:		Development/Python
URL:		https://github.com/notatallshaw/nab
Source0:	https://files.pythonhosted.org/packages/source/n/nab-markersets/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Marker sets for nab. The packaging backend is optional and is not required.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
