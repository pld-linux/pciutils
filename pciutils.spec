Summary:	Linux PCI Utilities
Summary(pl):	Narzêdzia do manipulacji ustawieniami urz±dzeñ PCI
Name:		pciutils
Version:	2.1.6
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch0:		pciutils-FHS.patch
Patch1:		pciutils-bufsiz.patch
Patch2:		pciutils-devel.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
You need thics package if (and probably only if) you are going to
build PLD-installer

%decription -l pl devel
Parwdowpodobnie jedynym powodem dla ktorego mozesz potrzebowac tego pakietu
jest kompilacja instalatora PLD


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir} \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}
make install-devel \
        DESTDIR=$RPM_BUILD_ROOT \
        datadir=%{_datadir} \
        mandir=%{_mandir} \
        sbindir=%{_sbindir} \
        libdir=%{_libdir} \
        includedir=%{_includedir}
						

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

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpci.a
%{_includedir}/pci/*.h
