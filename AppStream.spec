#
# Conditional build:
%bcond_without	apidocs		# API documentation build
%bcond_without	vala		# Vala API (VAPI)
#
Summary:	AppStream-Core library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia AppStream-Core
Name:		AppStream
Version:	0.6.2
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	http://www.freedesktop.org/software/appstream/releases/%{name}-%{version}.tar.gz
# Source0-md5:	c5df357df76156f7a6d4dd9a27b50b66
URL:		http://www.freedesktop.org/wiki/Distributions/AppStream/Software/
BuildRequires:	PackageKit-devel
BuildRequires:	cmake >= 2.8.6
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
%{?with_vala:BuildRequires:	vala}
BuildRequires:	xapian-core-devel >= 1.2
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

%build
install -d build
cd build
%cmake .. \
	%{?with_apidocs:-DDOCUMENTATION=ON} \
	%{?with_vala:-DVAPI=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README RELEASE
%attr(755,root,root) %{_bindir}/appstream-index
%attr(755,root,root) %{_bindir}/appstream-validate
%attr(755,root,root) %{_libdir}/libappstream.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream.so.0
%{_libdir}/girepository-1.0/Appstream-0.6.typelib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/appstream.conf
%dir %{_datadir}/app-info
%{_datadir}/app-info/categories.xml
%{_mandir}/man1/appstream-index.1*
%{_mandir}/man1/appstream-validate.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream.so
%{_datadir}/gir-1.0/Appstream-0.6.gir
%{_includedir}/Appstream
%{_pkgconfigdir}/appstream.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*
%endif

%if %{with vala}
%files -n vala-appstream
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/appstream.vapi
%endif

%files -n PackageKit-plugin-appstream
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/packagekit-plugins/libpk_plugin_appstream.so
