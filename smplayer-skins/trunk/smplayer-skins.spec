%define name    smplayer-skins
%define version 15.2.0
%define release rvm

Name:           %{name}
Summary:        Skins for SMPlayer
License:        GPL
Group:          Applications/Multimedia
URL:            http://smplayer.sourceforge.net/
Version:        %{version}
Release:        %{release}

Source0:        %{name}-%{version}.tar.bz2

Packager:       Ricardo Villalba <rvm@users.sourceforge.net>
Distribution:   SUSE Linux 9.2 (i586)
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
Autoreqprov:    On
Requires:		smplayer >= 0.8.2

%description
This package provides skin themes for SMPlayer.
SMPlayer is a graphical user interface (GUI) for the award-winning mplayer
and also for mpv. But apart from providing access for the most common
and useful options of mplayer and mpv, SMPlayer adds other interesting features
like the possibility to play Youtube videos or search and download subtitles.
One of the main features is the ability to remember the state of a
played file, so when you play it later it will be resumed at the same point
and with the same settings.

%prep
%setup -q

%install
make PREFIX=/usr DESTDIR=%{?buildroot:%{buildroot}} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr (-,root,root) /*

%changelog
* Sun Oct 28 2012 Ricardo Villalba <rvm@users.sourceforge.net>
  - first spec file
