Summary:	Linux PCI Utilities
Summary(pl):	Narzêdzia do manipulacji ustawieniami urz±dzeñ PCI
Name:		pciutils
Version:	2.1.8
Release:	19
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-bufsiz.patch
Patch2:		%{name}-devel.patch
Patch3:		%{name}-pci.ids-update.patch
Patch4:		%{name}-qlogic.patch
Patch5:		%{name}-pcix.patch
Patch6:		%{name}-ids-2.patch
Patch7:		%{name}-i815.patch
Patch8:		%{name}-ati.patch
Patch9:		%{name}-vortex.patch
Patch10:	%{name}-megaraid.patch
Patch11:	%{name}-2.4.0.diffs
Patch12:	%{name}-broadcom.patch
Patch13:	%{name}-man.patch
Patch14:	%{name}-i860.patch
Patch15:	%{name}-serveraid.patch
Patch16:	%{name}-various.ids.patch
Patch17:	%{name}-lsi.patch
Patch18:	%{name}-moremega.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/lib
%define		_datadir	%{_prefix}/share/misc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l pl
Pakiet zawiera narzêdzia do ustawiania i odczytywania informacji o
urz±dzeniach pod³±czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udostêpniaj±cego odpowiednie informacje
poprzez /proc/bus/pci).

%package devel
Summary:	pciutils developement files (for PLD-installer)
Summary(pl):	pliki developerskie pciutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
You need this package if (and probably only if) you are going to build
PLD-installer.

%decription -l pl devel
Prawdopodobnie jedynym powodem dla którego mo¿esz potrzebowaæ tego pakietu
jest kompilacja instalatora PLD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p0
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir} \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}
%{__make} install-devel \
        DESTDIR=$RPM_BUILD_ROOT \
        datadir=%{_datadir} \
        mandir=%{_mandir} \
        sbindir=%{_sbindir} \
        libdir=%{_libdir} \
        includedir=%{_includedir}
						
gzip -9nf README ChangeLog pciutils.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/pci.ids
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpci.a
%dir %{_includedir}/pci
%{_includedir}/pci/*.h
