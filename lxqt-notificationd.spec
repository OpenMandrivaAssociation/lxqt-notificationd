%define git 0

Name: lxqt-notificationd
Version: 1.2.0
%if %git
Source0: %{name}-%{git}.tar.xz
Release: 1.%{git}.1
%else
Source0: https://github.com/lxqt/lxqt-notificationd/releases/download/%{version}/lxqt-notificationd-%{version}.tar.xz
Release: 3
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
Provides: virtual-notification-daemon

%description
Notification daemon for the LXQt desktop.

%prep
%autosetup -p1

%cmake_qt5 \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-G Ninja

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
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
