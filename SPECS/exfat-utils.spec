Name:           exfat-utils
Summary:        Utilities for exFAT file system
Version:        1.2.4
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/exfat-utils-%{version}.tar.gz
URL:            https://github.com/relan/exfat

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR="$RPM_BUILD_ROOT"
ln -s %{_mandir}/man8/exfatfsck.8.gz %{buildroot}/%{_mandir}/man8/fsck.exfat.8.gz
ln -s %{_mandir}/man8/mkexfatfs.8.gz %{buildroot}/usr/share/man/man8/mkfs.exfat.8.gz

%files
%doc COPYING
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%{_sbindir}/mkfs.exfat
%{_sbindir}/exfatlabel
%{_mandir}/man8/*

%changelog
* Mon Sep 26 2016 Dario Cordova <dcordova@deskosproject.org> - 1.2.4-1
- Initial package for DeskOS
