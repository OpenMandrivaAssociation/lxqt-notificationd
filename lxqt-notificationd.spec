%define git 0

Name: lxqt-notificationd
Version: 0.10.0
%if %git
Source0: %{name}-%{git}.tar.xz
Release: 1.%{git}.1
%else
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
Release: 2
%endif
Summary: Notification daemon for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(lxqt)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(Qt5LinguistTools)

%description
Notification daemon for the LXQt desktop.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build


%find_lang lxqt-config-notificationd --with-qt
%find_lang lxqt-notificationd --with-qt

%files -f lxqt-config-notificationd.lang -f lxqt-notificationd.lang
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_datadir}/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_*.qm
