Summary:	Linux PCI Utilities
Summary(pl):	NarzÍdzia do manipulacji ustawieniami urz±dzeÒ PCI
Name:		pciutils
Version:	2.1.9
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-bufsiz.patch
Patch2:		%{name}-devel.patch
Patch3:		%{name}-qlogic.patch
Patch4:		%{name}-pcix.patch
Patch5:		%{name}-man.patch
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
Pakiet zawiera narzÍdzia do ustawiania i odczytywania informacji o
urz±dzeniach pod≥±czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udostÍpniaj±cego odpowiednie informacje
poprzez /proc/bus/pci).

%package devel
Summary:	pciutils development files (for PLD-installer)
Summary(pl):	pliki developerskie pciutils
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description devel
You need this package if (and probably only if) you are going to build
PLD-installer.

%description -l pl devel
Prawdopodobnie jedynym powodem dla ktÛrego moøesz potrzebowaÊ tego pakietu
jest kompilacja instalatora PLD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci	$RPM_BUILD_ROOT%{_sbindir}
install *.h lib/[ch]*.h	$RPM_BUILD_ROOT%{_includedir}/pci
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids		$RPM_BUILD_ROOT%{_datadir}
install lib/libpci.a	$RPM_BUILD_ROOT%{_libdir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
						
gzip -9nf README ChangeLog pciutils.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/pci.ids
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%lang(ja) %{_mandir}/ja/man8/*
%lang(pl) %{_mandir}/pl/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpci.a
%dir %{_includedir}/pci
%{_includedir}/pci/*.h
