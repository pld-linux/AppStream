#
# Conditional build:
%bcond_without	apidocs		# API documentation build
%bcond_with	apt		# Debian/APT support
%bcond_without	qt		# Qt library (libappstream-qt)
%bcond_without	vala		# Vala API (VAPI)

Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	0.9.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
# Source0-md5:	a7f0312c39a7eb6c557c4126a4d71cf6
URL:		https://www.freedesktop.org/wiki/Distributions/AppStream/
BuildRequires:	cmake >= 3.2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	protobuf-devel
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala}
BuildRequires:	xapian-core-devel >= 1.2
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.0
BuildRequires:	qt5-qmake >= 5.0
%endif
%if %{with apidocs}
BuildRequires:	gtk-doc
BuildRequires:	publican
BuildRequires:	xmlto
%endif
Requires:	glib2 >= 1:2.36
Requires:	xapian-core-libs >= 1.2
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
Requires:	glib2-devel >= 1:2.36

%description devel
Header files for AppStream library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStream.

%package apidocs
Summary:	AppStream API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki AppStream
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for AppStream library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki AppStream.

%package qt
Summary:	AppstreamQt library
Summary(pl.UTF-8):	Biblioteka AppstreamQt
Group:		Libraries
Requires:	Qt5Core >= 5.0
Requires:	xapian-core-libs >= 1.2

%description qt
AppstreamQt library.

%description qt -l pl.UTF-8
Biblioteka AppstreamQt.

%package qt-devel
Summary:	Header files for AppstreamQt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppstreamQt
Group:		Libraries
Requires:	%{name}-qt = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0

%description qt-devel
Header files for AppstreamQt library.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppstreamQt.

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-appstream
Vala API for AppStream library.

%description -n vala-appstream -l pl.UTF-8
API języka Vala do biblioteki AppStream.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	%{?with_apt:-DAPT_SUPPORT=ON} \
	%{?with_apidocs:-DDOCUMENTATION=ON} \
	%{?with_qt:-DQT=ON} \
	%{?with_vala:-DVAPI=ON}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %ghost %{_libdir}/libappstream.so.3
%{_libdir}/girepository-1.0/AppStream-1.0.typelib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/appstream.conf
%dir %{_datadir}/app-info
%{_datadir}/app-info/categories.xml
%if %{with apt}
/etc/apt/apt.conf.d/50appstream
%endif
%{_mandir}/man1/appstreamcli.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream.so
%{_datadir}/gir-1.0/AppStream-1.0.gir
%{_includedir}/AppStream
%{_pkgconfigdir}/appstream.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/appstream
%{_gtkdocdir}/appstream
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppstreamQt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAppstreamQt.so.1

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppstreamQt.so
%{_includedir}/AppstreamQt
%{_libdir}/cmake/AppstreamQt
%endif

%files -n gettext-its-metainfo
%defattr(644,root,root,755)
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/metainfo.its
%{_datadir}/gettext/its/metainfo.loc

%if %{with vala}
%files -n vala-appstream
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appstream.vapi
%endif
