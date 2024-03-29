#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		grantleetheme
Summary:	Grantlee Theme
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	95461cddadab088db7cc5664bc23f1ed
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	grantlee-qt5-devel >= 5.3
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildConflicts:	Qt6Dbus-devel
BuildConflicts:	Qt6Gui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GrantleeTheme library provides a class for loading theme packages
containing set of templates.

%description -l pl.UTF-8
Biblioteka GrantleeTheme dostarcza klasę do ładowania paczek
zawierających zestawy szablonów.

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=5
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/grantlee/5.3/kde_grantlee_plugin.so
%ghost %{_libdir}/libKPim5GrantleeTheme.so.5
%attr(755,root,root) %{_libdir}/libKPim5GrantleeTheme.so.*.*.*
%{_datadir}/qlogging-categories5/grantleetheme.categories
%{_datadir}/qlogging-categories5/grantleetheme.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/qt5/mkspecs/modules/qt_GrantleeTheme.pri
%{_includedir}/KPim5/GrantleeTheme
%{_libdir}/cmake/KPim5GrantleeTheme
%{_libdir}/libKPim5GrantleeTheme.so

