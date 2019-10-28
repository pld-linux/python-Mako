#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests

%define		fname	Mako
Summary:	Templating system for Python
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python-%{fname}
Version:	1.0.7
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mako/
Source0:	https://files.pythonhosted.org/packages/source/M/Mako/%{fname}-%{version}.tar.gz
# Source0-md5:	5836cc997b1b773ef389bf6629c30e65
Patch0:		%{name}-mock.patch
URL:		http://www.makotemplates.org/
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-markupsafe >= 0.9.2
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-markupsafe >= 0.9.2
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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

%package -n python3-%{fname}
Summary:	Templating system for Python
Summary(pl.UTF-8):	System szablonów dla języka Python
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{fname}
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance.

%description -n python3-%{fname} -l pl.UTF-8
Mako jest biblioteką szablonów napisaną w języku Python. Zapewnia
przyjazną, nie XML-ową składnię, która jest kompilowana do modułów
Pythona dla zwiększenia wydajności.

%package doc
Summary:	Documentation for Python Mako module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona Mako
Group:		Documentation

%description doc
Documentation for Python Mako module.

%description doc -l pl.UTF-8
Dokumentacja do modułu Pythona Mako.

%prep
%setup -qn %{fname}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/mako-render{,-2}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/mako-render{,-3}
%endif

%if %{with python2}
ln -sf mako-render-2 $RPM_BUILD_ROOT%{_bindir}/mako-render
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%attr(755,root,root) %{_bindir}/mako-render
%attr(755,root,root) %{_bindir}/mako-render-2
%{py_sitescriptdir}/mako
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{fname}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%attr(755,root,root) %{_bindir}/mako-render-3
%{py3_sitescriptdir}/mako
%{py3_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc doc/{_static,*.html,*.js}
