Summary:	Linux PCI Utilities
Summary(pl):	Narzêdzia do manipulacji ustawieniami urz±dzeñ PCI
Name:		pciutils
Version:	2.1.2
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch:		pciutils-FHS.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
Buildroot:	/tmp/%{name}-%{version}-root

%define		_exec_prefix	/
%define		_datadir	%{_prefix}/share/misc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or newer
(supporting the /proc/bus/pci interface).

%description -l pl
Pakiet zawiera narzêdzia do ustawiania i odczytywania informacji o
urz±dzeniach pod³±czonych do szyny PCI w Twoim komputerze. Wymaga kernela
2.1.82 lub nowszego (udostêpniaj±cego odpowiednie informacje poprzez
/proc/bus/pci).

%prep
%setup -q
%patch -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8}

make install \
	ROOT=$RPM_BUILD_ROOT \
	datadir=%{_datadir} \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

strip $RPM_BUILD_ROOT%{_sbindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README ChangeLog pciutils.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/pci.ids
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
