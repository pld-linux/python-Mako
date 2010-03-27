# TODO:
# - examples subpackage
#
%bcond_without	python2
%bcond_without	python3
#
%define		fname	Mako
Summary:	Templating system for Python
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python-%{fname}
Version:	0.3.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/Mako/%{fname}-%{version}.tar.gz
# Source0-md5:	4fc68467ee226111e102510054ae1e51
URL:		http://www.makotemplates.org/
%if %{with python2}
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
%pyrequires_eq	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-distribute
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%description -n python3-%{fname}
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance.

%description -n python3-%{fname} -l pl.UTF-8
Mako jest biblioteką szablonów napisaną w języku Python. Zapewnia
przyjazną, nie XML-ową składnię, która jest kompilowana do modułów
Pythona dla zwiększenia wydajności.

%prep
%setup -qn %{fname}-%{version}

%build
%if %{with python2}
%{__python} setup.py build -b build-2
%endif

%if %{with python3}
%{__python3} setup.py build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python2}
%{__python} setup.py \
	build -b build-2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/mako-render{,-2}

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build -b build-3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/mako-render{,-3}

%py3_postclean
%endif

ln -s mako-render-2 $RPM_BUILD_ROOT%{_bindir}/mako-render

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES PKG-INFO README
%attr(755,root,root) %{_bindir}/mako-render
%attr(755,root,root) %{_bindir}/mako-render-2
%{py_sitescriptdir}/mako
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{fname}
%defattr(644,root,root,755)
%doc CHANGES PKG-INFO README
%attr(755,root,root) %{_bindir}/mako-render-3
%{py3_sitescriptdir}/mako
%{py3_sitescriptdir}/%{fname}-%{version}-py*.egg-info
%endif
