Summary:	Manipulate the value of the idle3 timer found on recent WD Hard Disk Drives
Name:		idle3-tools
Version:	0.9.1
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/idle3-tools/%{name}-%{version}.tgz
# Source0-md5:	797d8775b80b7b7b67a1f8b0a5b41f30
URL:		http://idle3-tools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Idle3-tools provides a Linux/Unix utility that can disable, get and
set the value of the infamous idle3 timer found on recent Western
Digital Hard Disk Drives. It can be used as an alternative to the
official wdidle3.exe proprietary utility, without the need to reboot
in a DOS environement. A power off/on cycle of the drive will still be
mandatory for new settings to be taken into account.

Idle3-tools is an independant project, unrelated in any way to Western
Digital Corp.

WARNING: THIS SOFTWARE IS EXPERIMENTAL AND NOT WELL TESTED. IT
ACCESSES LOW LEVEL INFORMATION OF YOUR HARDDRIVE. USE AT YOUR OWN
RISK.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
CC="%{__cc}" \
%{__make} \
	LDFLAGS="%{rpmldflags}" \
	STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	binprefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_sbindir}/idle3ctl
%{_mandir}/man8/idle3ctl*
