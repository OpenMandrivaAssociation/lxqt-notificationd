#define git 0

Name: lxqt-notificationd
Version: 2.4.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-notificationd/releases/download/%{version}/lxqt-notificationd-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}2
Summary: Notification daemon for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildSystem: cmake
BuildOption: -DPULL_TRANSLATIONS:BOOL=OFF
BuildRequires: cmake(lxqt)
BuildRequires: cmake(qt6xdg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(LayerShellQt)
BuildRequires: lxqt-build-tools
BuildRequires: git-core
Provides: virtual-notification-daemon

%description
Notification daemon for the LXQt desktop.

%build -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%files -f %{name}.lang
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
