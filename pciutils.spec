Summary:	Linux PCI Utilities
Summary(es):	Utilitarios Linux para PCI
Summary(pl):	NarzЙdzia do manipulacji ustawieniami urz╠dzeЯ PCI
Summary(pt_BR):	UtilitАrios para PCI do Linux
Summary(uk):	Утил╕ти роботи з PCI пристроями
Summary(ru):	Утилиты работы с PCI устройствами
Name:		pciutils
Version:	2.1.10
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Source2:	http://pciids.sourceforge.net/pci.ids
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-bufsiz.patch
Patch2:		%{name}-devel.patch
Patch4:		%{name}-man.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/lib
%define		_datadir	%{_prefix}/share/misc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l es
Utilitarios Linux para PCI.

%description -l pl
Pakiet zawiera narzЙdzia do ustawiania i odczytywania informacji o
urz╠dzeniach podЁ╠czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udostЙpniaj╠cego odpowiednie informacje
poprzez /proc/bus/pci).

%description -l pt_BR
Este pacote contИm vАrios utilitАrios para inspeГЦo e configuraГЦo de
dispositivos conectados ao barramento PCI do seu computador.

%description -l ru
Пакет pciutils содержит утилиты для инспектирования и конфигурирования
устройств, подключенных к PCI шине.

Для работы этим утилитам необходимо наличие интерфейса /proc/bus/pci.

%description -l uk
Пакет pciutils м╕стить утил╕ти для ╕нспектування та конф╕гурування
пристро╖в, п╕д'╓днаних до PCI шини.

Для роботи ц╕ утил╕ти потребують наявност╕ ╕нтерфейсу /proc/bus/pci.

%package devel
Summary:	pciutils development files (for PLD-installer)
Summary(es):	Biblioteca de desarrollo para aplicaciones que trabajan con el bus PCI en Linux
Summary(pl):	pliki developerskie pciutils
Summary(pt_BR):	Biblioteca de desenvolvimentos para aplicaГУes que trabalhem com o barramento PCI no Linux
Summary(ru):	Хедеры и другие файлы для разработки программ, работающих с шиной PCI
Summary(uk):	Хедери та ╕нш╕ файли для розробки програм, що працюють з шиною PCI
Group:		Development/Libraries

%description devel
You need this package if (and probably only if) you are going to build
PLD-installer.

%description devel -l es
Biblioteca de desarrollo para aplicaciones que trabajen con el bus PCI
en Linux.

%description devel -l pl
Prawdopodobnie jedynym powodem dla ktСrego mo©esz potrzebowaФ tego
pakietu jest kompilacja instalatora PLD.

%description devel -l pt_BR
Biblioteca de desenvolvimentos para aplicaГУes que trabalhem com o
barramento PCI no Linux.

%description devel -l ru
Этот пакет содержит хедеры и другие файлы для разработки программ
инспектирующих и конфигурирующих устройства, подключенные к шине PCI.

%description devel -l uk
Цей пакет м╕стить хедери та ╕нш╕ файли для розробки програм, що
╕нспектують та конф╕гурують пристро╖, п╕д'╓днан╕ до шини PCI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
# paranoid check whether pci.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE2}`" -lt "`wc -l < pci.ids`" ] ; then
	echo "pci.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE2} .
%{__make} OPT="%{rpmcflags} -fomit-frame-pointer"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci	$RPM_BUILD_ROOT%{_sbindir}
install *.h lib/[ch]*.h	$RPM_BUILD_ROOT%{_includedir}/pci
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids		$RPM_BUILD_ROOT%{_datadir}
install lib/libpci.a	$RPM_BUILD_ROOT%{_libdir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
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
