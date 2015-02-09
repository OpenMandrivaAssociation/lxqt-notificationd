%define git 0

Name: lxqt-notificationd
Version: 0.9.0
%if %git
Source0: %{name}-%{git}.tar.xz
Release: 0.%{git}.1
%else
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Release: 1
%endif
Summary: Notification daemon for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: qt5-devel

%description
Notification daemon for the LXQt desktop

%prep
%setup -q
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/lxqt-notificationd
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
