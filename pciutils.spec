Summary:	Linux PCI Utilities
Summary(pl):	Narzędzia do manipulacji ustawieniami urządzeń PCI
Name:		pciutils
Version:	1.99.5
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzędzia/System
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/alpha/%{name}-%{version}.tar.gz
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or newer
(supporting the /proc/bus/pci interface).

%description -l pl
Pakiet zawiera narzędzia do ustawiania i odczytywania informacji o
urządzeniach podłączonych do szyny PCI w Twoim komputerze. Wymaga kernela
2.1.82 lub nowszego (udostępniającego odpowiednie informacje poprzez
/proc/bus/pci).

%prep
%setup -q

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,/usr/{man/man8,share}}

install -s lspci setpci $RPM_BUILD_ROOT/sbin
install lspci.8 setpci.8 $RPM_BUILD_ROOT/usr/man/man8
install pci.ids $RPM_BUILD_ROOT/usr/share

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/* \
	README ChangeLog pciutils.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
/usr/share/pci.ids
%attr(755,root,root) /sbin/*
/usr/man/man8/*

%changelog
* Sun May  2 1999 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [1.99.5-1]
- added gzippping %doc and man pages,
- added Group(pl),
- pci.ids moved to /usr/share and removed trom them %config (this data file,
  not %config).

* Mon Oct 26 1998 Wojtek Ślusarczyk <wojtek@shadow.eu.org>
  [1.08-1d]
- updated to 1.08,
- minor changes.

* Tue Sep 29 1998 Krzysztof G. Baranowski <kgb@knm.org.pl>
  [1.07-1d]
- build from non-root account against glibc-2.1,
- written spec from scratch.
