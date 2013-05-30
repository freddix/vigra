Summary:	Generic Programming for Computer Vision
Name:		vigra
Version:	1.9.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://hci.iwr.uni-heidelberg.de/vigra/%{name}-%{version}-src.tar.gz
# Source0-md5:	b6155afe1ea967917d2be16d98a85404
URL:		http://hci.iwr.uni-heidelberg.de/vigra/
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	fftw3-single-devel
#BuildRequires:	hdf5-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures. By using template techniques similar
to those in the C++ Standard Template Library, you can easily adapt
any VIGRA component to the needs of your application, without thereby
giving up execution speed.

%package devel
Summary:	Header files for vigra library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to compile programs with vigra.

%package -n python-vigra
Summary:	VIGRA Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-numpy
Suggests:	python-PyQt4

%description -n python-vigra
VIGRA Python bindings.

%package doc
Summary:	Development documentation for vigra library
Group:		Documentation

%description doc
Development documentation for vigra library.

%prep
%setup -q

%build
%cmake . \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/vigra
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/vigra
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/vigra*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%attr(755,root,root) %ghost %{_libdir}/libvigraimpex.so.4
%attr(755,root,root) %{_libdir}/libvigraimpex.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vigra-config
%attr(755,root,root) %{_libdir}/libvigraimpex.so
%{_includedir}/vigra
%dir %{_libdir}/vigra
%{_libdir}/vigra/VigraConfig*.cmake
%{_libdir}/vigra/vigra-targets*.cmake

%files -n python-vigra
%defattr(644,root,root,755)
%dir %{py_sitedir}/vigra
%dir %{py_sitedir}/vigra/pyqt
%attr(755,root,root) %{py_sitedir}/vigra/*.so
%{py_sitedir}/vigra/*.py[co]
%{py_sitedir}/vigra/pyqt/*.py[co]

%files doc
%defattr(644,root,root,755)
%doc doc/{vigra,vigranumpy}

