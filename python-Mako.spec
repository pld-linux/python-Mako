%define		fname	Mako
Summary:	Templating system for Python
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python-%{fname}
Version:	0.3.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/Mako/%{fname}-%{version}.tar.gz
# Source0-md5:	910550812aba6b3e05ffe15c3f68199e
URL:		http://www.makotemplates.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance.

%description -l pl.UTF-8
Mako jest biblioteką szablonów napisaną w języku Python. Zapewnia
przyjazną, nie XML-ową składnię, która jest kompilowana do modułów
Pythona dla zwiększenia wydajności.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PKG-INFO README
%attr(755,root,root) %{_bindir}/mako-render
%{py_sitescriptdir}/mako
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
