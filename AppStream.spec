#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	apt		# Debian/APT support
%bcond_without	compose		# appstream-compose library
%bcond_without	qt		# Qt libraries (any)
%bcond_without	qt5		# Qt5 library (libAppStreamQt5)
%bcond_without	qt6		# Qt6 library (libAppStreamQt)
%bcond_without	static_libs	# static libraries
%bcond_without	systemd		# systemd
%bcond_without	vala		# Vala API (VAPI)

%if %{without qt}
%undefine	with_qt5
%undefine	with_qt6
%endif
Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	1.0.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
# Source0-md5:	a9f9b45b9a3b2125148821b42b218d77
URL:		https://www.freedesktop.org/wiki/Distributions/AppStream/
BuildRequires:	curl-devel >= 7.62
%{?with_apidocs:BuildRequires:	daps}
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gettext-tools
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.62
BuildRequires:	gobject-introspection-devel >= 1.56
BuildRequires:	gperf
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	itstool
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libstemmer-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxmlb-devel >= 0.3.14
BuildRequires:	libxslt-progs
# with .pc file
BuildRequires:	lmdb-devel >= 0.9.24-1
BuildRequires:	meson >= 0.62
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.750
BuildRequires:	sed >= 4
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala}
BuildRequires:	xmlto
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
BuildRequires:	zstd-devel
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.15
BuildRequires:	Qt5Test-devel >= 5.15
BuildRequires:	qt5-build >= 5.15
BuildRequires:	qt5-qmake >= 5.15
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6.2.4
BuildRequires:	Qt6Test-devel >= 6.2.4
BuildRequires:	qt6-build >= 6.2.4
BuildRequires:	qt6-qmake >= 6.2.4
%endif
%if %{with compose}
BuildRequires:	cairo-devel >= 1.12
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.48
BuildRequires:	pango-devel
%endif
Requires:	curl-libs >= 7.62
Requires:	glib2 >= 1:2.62
Requires:	libxmlb >= 0.3.14
Obsoletes:	PackageKit-plugin-appstream < 0.7.4
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
Requires:	glib2-devel >= 1:2.62

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
Requires:	librsvg >= 2.48

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

%package qt5
Summary:	AppStreamQt5 library
Summary(pl.UTF-8):	Biblioteka AppStreamQt5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 5.15
Obsoletes:	AppStream-qt < 1

%description qt5
AppStreamQt5 library.

%description qt5 -l pl.UTF-8
Biblioteka AppStreamQt5.

%package qt5-devel
Summary:	Header files for AppStreamQt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStreamQt5
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.15
Obsoletes:	AppStream-qt-devel < 1

%description qt5-devel
Header files for AppStreamQt5 library.

%description qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStreamQt5.

%package qt5-static
Summary:	Static AppStreamQt5 library
Summary(pl.UTF-8):	Statyczna biblioteka AppStreamQt5
Group:		Development/Libraries
Requires:	%{name}-qt5-devel = %{version}-%{release}
Obsoletes:	AppStream-qt-static < 1

%description qt5-static
Static AppStreamQt5 library.

%description qt5-static -l pl.UTF-8
Statyczna biblioteka AppStreamQt5.

%package qt6
Summary:	AppStreamQt library
Summary(pl.UTF-8):	Biblioteka AppStreamQt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core >= 6.2.4

%description qt6
AppStreamQt library.

%description qt6 -l pl.UTF-8
Biblioteka AppStreamQt.

%package qt6-devel
Summary:	Header files for AppStreamQt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStreamQt
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt6 = %{version}-%{release}
Requires:	Qt6Core-devel >= 6.2.4

%description qt6-devel
Header files for AppStreamQt library.

%description qt6-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStreamQt.

%package qt6-static
Summary:	Static AppStreamQt library
Summary(pl.UTF-8):	Statyczna biblioteka AppStreamQt
Group:		Development/Libraries
Requires:	%{name}-qt6-devel = %{version}-%{release}

%description qt6-static
Static AppStreamQt library.

%description qt6-static -l pl.UTF-8
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

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Dapidocs=%{__true_false apidocs} \
	%{?with_apt:-Dapt-support=true} \
	%{?with_compose:-Dcompose=true} \
	-Ddocs=%{__true_false apidocs} \
	-Dgir=true \
	-Dinstall-docs=%{__true_false apidocs} \
	%{?with_qt:-Dqt=true} \
	%{?with_qt:-Dqt-versions="[%{?with_qt5:'5'%{?with_qt6:,}}%{?with_qt6:'6'}]"} \
	-Dstemming=true \
	%{!?with_systemd:-Dsystemd=false} \
	%{?with_vala:-Dvapi=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_docdir}
%{?with_apidocs:%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc $RPM_BUILD_ROOT%{_docdir}}

# unify; bn_BD is more complete than bn
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/bn
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{bn_BD,bn}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ain,rom}

# Unneeded test file
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/installed-tests

%find_lang appstream

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	compose -p /sbin/ldconfig
%postun	compose -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%post	qt6 -p /sbin/ldconfig
%postun	qt6 -p /sbin/ldconfig

%files -f appstream.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md RELEASE
%attr(755,root,root) %{_bindir}/appstreamcli
%attr(755,root,root) %{_libdir}/libappstream.so.*.*
%ghost %{_libdir}/libappstream.so.5
%{_libdir}/girepository-1.0/AppStream-1.0.typelib
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/appstream.conf
%{_datadir}/metainfo/org.freedesktop.appstream.cli.metainfo.xml
%if %{with apt}
%{_sysconfdir}/apt/apt.conf.d/50appstream
%endif
%{_mandir}/man1/appstreamcli.1*
%dir %{_datadir}/appstream
%{_datadir}/appstream/appstream.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream.so
%{_datadir}/gir-1.0/AppStream-1.0.gir
%{_includedir}/appstream
%{_pkgconfigdir}/appstream.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libappstream.a
%endif

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
%{_gtkdocdir}/appstream-compose
%endif

%if %{with compose}
%files compose
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/appstreamcli-compose
%attr(755,root,root) %{_libdir}/libappstream-compose.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-compose.so.0
%{_libdir}/girepository-1.0/AppStreamCompose-1.0.typelib
%{_datadir}/metainfo/org.freedesktop.appstream.compose.metainfo.xml
%{_mandir}/man1/appstreamcli-compose.1*

%files compose-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-compose.so
%{_includedir}/appstream-compose
%{_datadir}/gir-1.0/AppStreamCompose-1.0.gir
%{_pkgconfigdir}/appstream-compose.pc

%if %{with static_libs}
%files compose-static
%defattr(644,root,root,755)
%{_libdir}/libappstream-compose.a
%endif
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAppStreamQt5.so.3

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt5.so
%{_includedir}/AppStreamQt5
%{_libdir}/cmake/AppStreamQt5

%if %{with static_libs}
%files qt5-static
%defattr(644,root,root,755)
%{_libdir}/libAppStreamQt5.a
%endif
%endif

%if %{with qt6}
%files qt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libAppStreamQt.so.3

%files qt6-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppStreamQt.so
%{_includedir}/AppStreamQt
%{_libdir}/cmake/AppStreamQt

%if %{with static_libs}
%files qt6-static
%defattr(644,root,root,755)
%{_libdir}/libAppStreamQt.a
%endif
%endif

%files -n gettext-its-metainfo
%defattr(644,root,root,755)
%{_datadir}/gettext/its/metainfo.its
%{_datadir}/gettext/its/metainfo.loc
