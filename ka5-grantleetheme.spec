%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		grantleetheme
Summary:	Grantlee Theme
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a4b9bc2e70c080a33f2fa2b07df417d7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GrantleeTheme library provides a class for loading theme packages
containing set of templates.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/grantleetheme.categories
/etc/xdg/grantleetheme.renamecategories
%attr(755,root,root) %{_libdir}/grantlee/5.1/kde_grantlee_plugin.so
%attr(755,root,root) %ghost %{_libdir}/libKF5GrantleeTheme.so.5
%attr(755,root,root) %{_libdir}/libKF5GrantleeTheme.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/GrantleeTheme
%{_includedir}/KF5/grantleetheme
%{_includedir}/KF5/grantleetheme_version.h
%{_libdir}/cmake/KF5GrantleeTheme
%attr(755,root,root) %{_libdir}/libKF5GrantleeTheme.so
%{_libdir}/qt5/mkspecs/modules/qt_GrantleeTheme.pri
