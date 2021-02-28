#
# Conditional build:
%bcond_without	apidocs		# API documentation build
%bcond_with	apt		# Debian/APT support
%bcond_without	qt		# Qt library (libappstream-qt)
%bcond_without	vala		# Vala API (VAPI)

Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	0.12.10
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
# Source0-md5:	cd27ff2139bef3942529d9bd5329fd3a
URL:		https://www.freedesktop.org/wiki/Distributions/AppStream/
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gobject-introspection-devel >= 1.54
BuildRequires:	gperf
BuildRequires:	itstool
BuildRequires:	libsoup-devel >= 2.56
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libstemmer-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
# with .pc file
BuildRequires:	lmdb-devel >= 0.9.24-1
BuildRequires:	meson >= 0.48
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	sed >= 4
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala}
BuildRequires:	xmlto
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	Qt5Test-devel >= 5.0
BuildRequires:	qt5-build >= 5.0
BuildRequires:	qt5-qmake >= 5.0
%endif
%if %{with apidocs}
BuildRequires:	gtk-doc
BuildRequires:	publican
BuildRequires:	python3
%endif
Requires:	glib2 >= 1:2.58
Requires:	libsoup >= 2.56
Obsoletes:	PackageKit-plugin-appstream
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppStream-Core library and tools to access the AppStream component
database.

%description -l pl.UTF-8
Biblioteka i narzędzia AppStream-Core służące do dostępu do bazy
danych komponentu AppStream.

%package devel
Summary:	Header files for AppStream library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStream
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.58

%description devel
Header files for AppStream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStream.

%package static
Summary:	Static AppStream library
Summary(pl.UTF-8):	Statyczna biblioteka AppStream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AppStream library.

%description static -l pl.UTF-8
Statyczna biblioteka AppStream.

%package apidocs
Summary:	AppStream API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki AppStream
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for AppStream library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki AppStream.

%package qt
Summary:	AppStreamQt library
Summary(pl.UTF-8):	Biblioteka AppStreamQt
Group:		Libraries
Requires:	Qt5Core >= 5.0

%description qt
AppStreamQt library.

%description qt -l pl.UTF-8
Biblioteka AppStreamQt.

%package qt-devel
Summary:	Header files for AppStreamQt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStreamQt
Group:		Libraries
Requires:	%{name}-qt = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0

%description qt-devel
Header files for AppStreamQt library.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStreamQt.

%package qt-static
Summary:	Static AppStreamQt library
Summary(pl.UTF-8):	Statyczna biblioteka AppStreamQt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description qt-static
Static AppStreamQt library.

%description qt-static -l pl.UTF-8
Statyczna biblioteka AppStreamQt.

%package -n gettext-its-metainfo
Summary:	AppStream metainfo ITS data for gettext tools
Summary(pl.UTF-8):	Dane ITS AppStream metainfo dla narzędzi gettext
Group:		Development/Tools
Requires:	gettext-tools >= 0.19

%description -n gettext-its-metainfo
AppStream metainfo ITS data for gettext tools.

%description -n gettext-its-metainfo -l pl.UTF-8
Dane ITS AppStream metainfo dla narzędzi gettext.

%package -n vala-appstream
Summary:	Vala API for AppStream library
Summary(pl.UTF-8):	API języka Vala do biblioteki AppStream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-appstream
Vala API for AppStream library.

%description -n vala-appstream -l pl.UTF-8
API języka Vala do biblioteki AppStream.

%prep
%setup -q

%if "%{cc_version}" < "9.0"
%{__sed} -i -e "s/'-Wno-error=deprecated-copy', //" meson.build
%endif

%build
%meson build \
	%{?with_apidocs:-Ddocs=true} \
	%{?with_apt:-Dapt-support=true} \
	%{?with_qt:-Dqt=true} \
	-Dgir=true \
	-Dstemming=true \
	%{?with_vala:-Dvapi=true}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

install -d $RPM_BUILD_ROOT%{_docdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc $RPM_BUILD_ROOT%{_docdir}

%find_lang appstream

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files -f appstream.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md RELEASE
%attr(755,root,root) %{_bindir}/appstreamcli
%attr(755,root,root) %{_libdir}/libappstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream.so.4
%{_libdir}/girepository-1.0/AppStream-1.0.typelib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/appstream.conf
%{_datadir}/metainfo/org.freedesktop.appstream.cli.metainfo.xml
%if %{with apt}
/etc/apt/apt.conf.d/50appstream
%endif
%{_mandir}/man1/appstreamcli.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream.so
%{_datadir}/gir-1.0/AppStream-1.0.gir
%{_includedir}/appstream
%{_pkgconfigdir}/appstream.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libappstream.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/appstream
%{_gtkdocdir}/appstream
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAppStreamQt.so.2

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt.so
%{_includedir}/AppStreamQt
%{_libdir}/cmake/AppStreamQt

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libAppStreamQt.a
%endif

%files -n gettext-its-metainfo
%defattr(644,root,root,755)
%{_datadir}/gettext/its/metainfo.its
%{_datadir}/gettext/its/metainfo.loc

%if %{with vala}
%files -n vala-appstream
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appstream.deps
%{_datadir}/vala/vapi/appstream.vapi
%endif
