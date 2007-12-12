%define name xmbmon
%define version 2.05
%define realversion 205
%define release %mkrel 3

Summary: A motherboad monitoring tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/%{name}%{realversion}.tar.gz
Patch1:	 %{name}-makefile.patch.bz2
Patch2:  %{name}%{realversion}_fflush.patch.bz2
License: BSD
Group: System/Kernel and hardware
Url: http://www.nt.phys.kyushu-u.ac.jp/shimizu/download/download.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxorg-x11-devel

%description
A motherboard monitoring tools that uses the SMI bus.
%prep
%setup -q -n %{name}%{realversion}
%patch1 -p0
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

