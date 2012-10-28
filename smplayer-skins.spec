%define name    smplayer-skins
%define version 20121028
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
SMPlayer intends to be a complete front-end for Mplayer, from basic features 
like playing videos, DVDs, and VCDs to more advanced features like support 
for Mplayer filters and more. One of the main features is the ability to 
remember the state of a played file, so when you play it later it will resume 
at the same point and with the same settings. smplayer is developed with 
the Qt toolkit, so it's multi-platform.

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
