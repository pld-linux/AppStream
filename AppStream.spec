#
# Conditional build:
%bcond_without	apidocs		# API documentation build
%bcond_without	qt		# Qt library (libappstream-qt)
%bcond_without	vala		# Vala API (VAPI)
#
Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	0.7.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.xz
# Source0-md5:	0626feadb9b64babda4a292ec9ebb684
Patch0:		%{name}-libdir.patch
URL:		http://www.freedesktop.org/wiki/Distributions/AppStream/Software/
BuildRequires:	PackageKit-devel
%{?with_qt:BuildRequires:	QtCore-devel >= 4.8.0}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt4-qmake >= 4.8.0}
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala}
BuildRequires:	xapian-core-devel >= 1.2
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	gtk-doc
BuildRequires:	publican
BuildRequires:	xmlto
%endif
Requires:	glib2 >= 1:2.36
Requires:	xapian-core-libs >= 1.2
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

%description apidocs
API documentation for AppStream library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki AppStream.

%package qt
Summary:	AppstreamQt library
Summary(pl.UTF-8):	Biblioteka AppstreamQt
Group:		Libraries
Requires:	QtCore >= 4.8.0
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
Requires:	QtCore-devel >= 4.8.0

%description qt-devel
Header files for AppstreamQt library.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppstreamQt.

%package -n vala-appstream
Summary:	Vala API for AppStream library
Summary(pl.UTF-8):	API języka Vala do biblioteki AppStream
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

%description -n vala-appstream
Vala API for AppStream library.

%description -n vala-appstream -l pl.UTF-8
API języka Vala do biblioteki AppStream.

%package -n PackageKit-plugin-appstream
Summary:	AppStream plugin for PackageKit
Summary(pl.UTF-8):	Wtyczka AppStream dla PackageKita
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	PackageKit

%description -n PackageKit-plugin-appstream
AppStream plugin for PackageKit. It refreshes the AppStream database
of available applications.

%description -n PackageKit-plugin-appstream -l pl.UTF-8
Wtyczka AppStream dla PackageKita. Odświeża bazę danych AppStream
dostępnych aplikacji.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
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
%doc AUTHORS MAINTAINERS NEWS README RELEASE
%attr(755,root,root) %{_bindir}/appstream-index
%attr(755,root,root) %{_bindir}/appstream-validate
%attr(755,root,root) %{_libdir}/libappstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream.so.1
%{_libdir}/girepository-1.0/Appstream-0.7.typelib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/appstream.conf
%dir %{_datadir}/app-info
%{_datadir}/app-info/categories.xml
%{_mandir}/man1/appstream-index.1*
%{_mandir}/man1/appstream-validate.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream.so
%{_datadir}/gir-1.0/Appstream-0.7.gir
%{_includedir}/Appstream
%{_pkgconfigdir}/appstream.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/appstream
%endif

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppstreamQt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAppstreamQt.so.0

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAppstreamQt.so
%{_includedir}/AppstreamQt
%{_libdir}/cmake/AppstreamQt
%endif

%if %{with vala}
%files -n vala-appstream
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appstream.vapi
%endif

%files -n PackageKit-plugin-appstream
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/packagekit-plugins/libpk_plugin_appstream.so
