#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	apt		# Debian/APT support
%bcond_without	compose		# appstream-compose library
%bcond_without	qt		# Qt library (libappstream-qt)
%bcond_without	vala		# Vala API (VAPI)

Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	0.14.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
# Source0-md5:	fc4c5b9d4c7ace29063e68d16040fbd1
URL:		https://www.freedesktop.org/wiki/Distributions/AppStream/
BuildRequires:	curl-devel >= 7.62
%{?with_apidocs:BuildRequires:	daps}
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gobject-introspection-devel >= 1.56
BuildRequires:	gperf
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libstemmer-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
# with .pc file
BuildRequires:	lmdb-devel >= 0.9.24-1
BuildRequires:	meson >= 0.48
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.750
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
%if %{with compose}
BuildRequires:	cairo-devel >= 1.12
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	pango-devel
%endif
Requires:	curl-libs >= 7.62
Requires:	glib2 >= 1:2.58
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

%package apidocs
Summary:	AppStream API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki AppStream
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for AppStream library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki AppStream.

%package compose
Summary:	AppStreamCompose library
Summary(pl.UTF-8):	Biblioteka AppStreamCompose
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo >= 1.12

%description compose
AppStreamCompose library contains helper functions to generate
AppStream metadata and auxiliary data.

%description compose -l pl.UTF-8
Biblioteka AppStreamCompose zawiera funkcje pomocnicze do generowania
metadanych AppStream oraz danych pomocniczych.

%package compose-devel
Summary:	Header files for AppStreamCompose library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStreamCompose
Group:		Development/Libraries
Requires:	%{name}-compose = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description compose-devel
Header files for AppStreamCompose library.

%description compose-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStreamCompose.

%package compose-static
Summary:	Static AppStreamCompose library
Summary(pl.UTF-8):	Statyczna biblioteka AppStreamCompose
Group:		Development/Libraries
Requires:	%{name}-compose-devel = %{version}-%{release}

%description compose-static
Static AppStreamCompose library.

%description compose-static -l pl.UTF-8
Statyczna biblioteka AppStreamCompose.

%package qt
Summary:	AppStreamQt library
Summary(pl.UTF-8):	Biblioteka AppStreamQt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
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

%prep
%setup -q

%if "%{_ver_lt '%{cc_version}' '9.0'}" == "1"
%{__sed} -i -e "s/'-Wno-error=deprecated-copy', //" meson.build
%endif

%build
%meson build \
	%{?with_apt:-Dapt-support=true} \
	%{?with_compose:-Dcompose=true} \
	%{?with_apidocs:-Ddocs=true} \
	-Dgir=true \
	%{?with_qt:-Dqt=true} \
	-Dstemming=true \
	%{?with_vala:-Dvapi=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_docdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc $RPM_BUILD_ROOT%{_docdir}

# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{bn_BD,bn}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ain,rom}

%find_lang appstream

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	compose -p /sbin/ldconfig
%postun	compose -p /sbin/ldconfig

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

%if %{with vala}
%files -n vala-appstream
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appstream.deps
%{_datadir}/vala/vapi/appstream.vapi
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/appstream
%{_gtkdocdir}/appstream
%endif

%if %{with compose}
%files compose
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-compose.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-compose.so.0
%{_libdir}/girepository-1.0/AppStreamCompose-1.0.typelib

%files compose-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-compose.so
%{_includedir}/appstream-compose
%{_datadir}/gir-1.0/AppStreamCompose-1.0.gir
%{_pkgconfigdir}/appstream-compose.pc

%files compose-static
%defattr(644,root,root,755)
%{_libdir}/libappstream-compose.a
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
