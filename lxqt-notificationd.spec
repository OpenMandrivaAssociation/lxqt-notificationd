%define git 0

Name: lxqt-notificationd
Version: 0.13.0
%if %git
Source0: %{name}-%{git}.tar.xz
Release: 1.%{git}.1
%else
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Release: 1
%endif
Summary: Notification daemon for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: lxqt-build-tools
BuildRequires: git-core

%description
Notification daemon for the LXQt desktop.

%prep
%setup -q

%cmake_qt5 -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%find_lang lxqt-config-notificationd --with-qt
%find_lang lxqt-notificationd --with-qt

%files -f lxqt-config-notificationd.lang -f lxqt-notificationd.lang
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_datadir}/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_*.qm
%{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop
