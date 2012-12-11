%define name xmbmon
%define version 2.05
%define realversion 205
%define release %mkrel 7

Summary: A motherboad monitoring tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/%{name}%{realversion}.tar.gz
Patch1:	 %{name}_2.05-6.patch.bz2
Patch2:  %{name}%{realversion}_fflush.patch.bz2
License: BSD
Group: System/Kernel and hardware
Url: http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/download.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: X11-devel

%description
A motherboard monitoring tools that uses the SMI bus.
%prep
%setup -q -n %{name}%{realversion}
%patch1 -p1
%patch2 -p0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

%makeinstall INST_DIR=$RPM_BUILD_ROOT/%{_bindir} INST_XDIR=$RPM_BUILD_ROOT/usr/X11R6/bin INST_XRDIR=/usr/X11R6/lib/X11/app-defaults
%make install-man INST_MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 INST_MANXDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mbmon
/usr/X11R6/bin/xmbmon
%doc /usr/X11R6/man/man1/xmbmon.1*
%doc %{_mandir}/man1/mbmon.1*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.05-7mdv2011.0
+ Revision: 615680
- the mass rebuild of 2010.1 packages

* Wed Jan 20 2010 Erwan Velu <erwan@mandriva.org> 2.05-6mdv2010.1
+ Revision: 494056
- Fixing build on x86_64 systems

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.05-4mdv2009.0
+ Revision: 222294
- fix buildrequires on x86_64
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- import xmbmon

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Jun 14 2006 Erwan Velu  <erwan@seanodes.com> 2.05-3mdk
- Rebuild

* Fri Feb 10 2006 Erwan Velu  <erwan@seanodes.com> 2.05-2mdk
- fflush patch
- rebuild
* Fri Nov 12 2004 Erwan Velu  <erwan@n4.mandrakesoft.com> 2.05-1mdk
- 2.05
- remove patch2
* Wed Aug 25 2004 Erwan Velu  <erwan@n4.mandrakesoft.com> 2.04-2mdk
- Apply official patch for ALI chipsets
* Wed May  5 2004 Erwan Velu  <erwan@n4.mandrakesoft.com> 2.04-1mdk
- First MDK Package
