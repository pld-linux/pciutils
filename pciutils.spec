Summary:	Linux PCI utilities
Summary(cs.UTF-8):	Linuxové utility pro PCI
Summary(da.UTF-8):	PCI-bus-relaterede værktøjer
Summary(de.UTF-8):	PCI-Bus verwandte Dienstprogramme
Summary(es.UTF-8):	Utilitarios Linux para PCI
Summary(fr.UTF-8):	Utilitaires relatifs au bus PCI
Summary(it.UTF-8):	Utility correlate al bus PCI
Summary(ja.UTF-8):	PCI バス関連ユーティリティ
Summary(ko.UTF-8):	PCI 버스 관련 유틸리티들
Summary(nb.UTF-8):	PCI-buss-relaterte verktøy
Summary(pl.UTF-8):	Narzędzia do manipulacji ustawieniami urządzeń PCI
Summary(pt.UTF-8):	Utilitários relacionados com o 'bus' PCI
Summary(pt_BR.UTF-8):	Utilitários para PCI do Linux
Summary(ru.UTF-8):	Утилиты работы с PCI устройствами
Summary(sv.UTF-8):	PCI-bussrelaterade verktyg
Summary(uk.UTF-8):	Утиліти роботи з PCI пристроями
Summary(zh_CN.UTF-8):	PCI 总线相关的工具。
Name:		pciutils
Version:	3.0.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
# Source0-md5:	ba7dd55e568e2ea27b8b8cc2e3d46597
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	1ac48f433b1995044e14c24513992211
Source2:	http://pciids.sourceforge.net/pci.ids
# NoSource2-md5:	
Patch0:		%{name}-pci_h.patch
Patch1:		%{name}-pcimodules.patch
Patch2:		%{name}-nowhich.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/%{_lib}
%define		_datadir	/etc
%define		_sbindir	/sbin

%define		specflags	-fomit-frame-pointer

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l cs.UTF-8
Balíček pciutils obsahuje různé programy pro prohlížení a nastavování
zařízení připojených na sběrnici PCI. Obsažené programy vyžadují jádro
verze 2.1.82 nebo novější (podporující rozhraní /proc/bus/pci).

%description -l da.UTF-8
Pakken pciutils indeholder forskellige værktøjer for at undresøge og
opsætte enheder koplet til PCI-bussen. Værktøjet kræver kerneversion
2.1.82 eller senere (som understøtter grænsefladen /proc/bus/pci).

%description -l de.UTF-8
Das pciutils Paket enthält verschiedene Dienstprogramme für das
Überprüfen und Konfigurieren von Geräten, die an den PCI-Bus
angeschlossen sind. Die bereitgestellten Dienstprogramme erfordern
Kernel Version 2.1.82 oder neuer (und die darin implementierte
Unterstützung der Schnittstelle /proc/bus/pci).

%description -l es.UTF-8
Este paquete contiene varias utilidades para controlar y configurar
los dispositivos conectados al bus PCI. Las utilidades ofrecidas en
este paquete requieren la versión 2.1.82 o una posterior del kernel
(necesita del soporte para la interfaz /proc/bus/pci).

%description -l fr.UTF-8
Le paquetage pciutils contient divers utilitaires permettant
d'inspecter et de paramétrer des périphériques connectés au bus PCI.
Les utilitaires fournis requièrent un noyau version 2.1.82 ou plus
récent (prenant en charge l'interface /proc/bus/pci).

%description -l id.UTF-8
Paket ini berisi berbagai utilitas untuk mengamati dan mengeset device
yang terhubung ke bus PCI. Utilitas yang disediakan ini membutuhkan
kernel versi 2.1.82 atau yang lebih baru (yaitu yang mendukung
antarmuka /proc/bus/pci).

%description -l is.UTF-8
Þessi pakki inniheldur ýmis tól til að skoða og setja tæki tengd PCI
rútunni. Tólin eru nauðsynleg fyrir kjarna 2.1.82 eða nýrri (styðja
/proc/bus/pci viðmótið).

%description -l it.UTF-8
Il pacchetto pciutils contiene varie utility per controllare e
configurare i dispositivi collegati al bus PCI. L'utility fornita in
questo pacchetto richiede la versione 2.1.82 o successiva del kernel
(richiede il supporto per l'interfaccia /proc/bus/pci).

%description -l ja.UTF-8
このパッケージには、PCI バスに接続されたデバイスを調査、設定するた
めの各種ユーティリティが含まれています。それらのユーティリティは、カー
ネルバージョン 2.1.82 以降 (/proc/bus/pci インターフェイスをサポート)
を必要とします。

%description -l pl.UTF-8
Pakiet zawiera narzędzia do ustawiania i odczytywania informacji o
urządzeniach podłączonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udostępniającego odpowiednie informacje
poprzez /proc/bus/pci).

%description -l pt.UTF-8
Este pacote contém vários utilitários para inspeccionar e configurar
os dispositivos ligados ao bus PCI. Os utilitários fornecidos precisam
dum núcleo ou 'kernel' versão 2.1.82 ou mais recente (que suporte a
interface /proc/bus/pci).

%description -l pt_BR.UTF-8
Este pacote contém vários utilitários para inspeção e configuração de
dispositivos conectados ao barramento PCI do seu computador.

%description -l ru.UTF-8
Пакет содержит различные утилиты для проверки и настройки устройств,
подключенных к шине PCI. Утилита требует ядро версии 2.1.82 (или более
новой версии), поддерживаюей интерфейс /proc/bus/pci.

%description -l sk.UTF-8
Tento balík obsahuje rozličné pomocné programy pre prehliadanie a
nastavovanie zariadení pripojených na PCI zbernicu. Nástroje vyžadujú
jadro s číslom verzie aspoň 2.1.82 (podporujúce rozhranie
/proc/bus/pci).

%description -l sv.UTF-8
Paketet pciutils innehåller olika verktyg för att inspektera och
ställa in enheter kopplade till PCI-bussen. Verktygen kräver
kärnversion 2.1.82 eller senare (som stödjer gränssnittet
/proc/bus/pci).

%description -l uk.UTF-8
Пакет pciutils містить утиліти для інспектування та конфігурування
пристроїв, під'єднаних до PCI шини. Для роботи ці утиліти потребують
наявності інтерфейсу /proc/bus/pci.

%package devel
Summary:	Linux PCI development library
Summary(cs.UTF-8):	Linuxová vývojová knihovna pro PCI
Summary(da.UTF-8):	Linux PCI udviklingsbibliotek
Summary(de.UTF-8):	Linux PCI-Entwicklungsbibliothek
Summary(es.UTF-8):	Biblioteca de desarrollo para aplicaciones que trabajan con el bus PCI en Linux
Summary(fr.UTF-8):	Bibliothèque de développement PCI Linux
Summary(id.UTF-8):	Library pengembangan PCI Linux
Summary(is.UTF-8):	PCI þróunaraðgerðasafn fyrir Linux
Summary(it.UTF-8):	Libreria di sviluppo PCI per Linux
Summary(ja.UTF-8):	Linux PCI 開発ライブラリ
Summary(ko.UTF-8):	Linux PCI 개발용 라이브러리
Summary(nb.UTF-8):	Linux PCI utviklingsbibliotek
Summary(pl.UTF-8):	Pliki developerskie pciutils
Summary(pt.UTF-8):	Biblioteca de desenvolvimento para PCI do Linux
Summary(pt_BR.UTF-8):	Biblioteca de desenvolvimentos para aplicações que trabalhem com o barramento PCI no Linux
Summary(ru.UTF-8):	Хедеры и другие файлы для разработки программ, работающих с шиной PCI
Summary(sk.UTF-8):	Knižnica pre vývoj PCI na Linuxe
Summary(sl.UTF-8):	Razvojna knjižnica za PCI v Linuxu
Summary(sv.UTF-8):	Linux PCI utvecklignsbibliotek
Summary(uk.UTF-8):	Хедери та інші файли для розробки програм, що працюють з шиною PCI
Summary(zh_CN.UTF-8):	Linux PCI 开发程序库。
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
This package contains a library for inspecting and setting devices
connected to the PCI bus.

%description devel -l cs.UTF-8
Tento balíček obsahuje knihovny pro prohlížení a nastavování zařízení
připojených k PCI sběrnici.

%description devel -l da.UTF-8
Denne pakke indeholder et bibliotek for at inspektere og stælla in
enheder kopplade til PCI-bussen.

%description devel -l de.UTF-8
Dieses Paket enthält eine Bibliothek für das Überprüfen und
Konfigurieren von Geräten, die an den PCI-Bus angeschlossen sind.

%description devel -l es.UTF-8
Biblioteca de desarrollo para aplicaciones que trabajen con el bus PCI
en Linux.

%description devel -l fr.UTF-8
Ce paquetage contient une bibliothèque permettant d'inspecter et de
définir des périphériques connectés au bus PCI.

%description devel -l id.UTF-8
Paket ini berisi library untuk mengamati dan mengeset device yang
terhubung ke bus PCI.

%description devel -l is.UTF-8
Þessi pakki inniheldur aðgerðasafn til að skoða og setja tæki tengd
PCI rútunni.

%description devel -l it.UTF-8
Questo pacchetto contiene una libreria per controllare e configurare i
dispositivi collegati al bus PCI.

%description devel -l ja.UTF-8
このパッケージには、PCI バスに接続されたデバイスを検査、設定
するためのライブラリが含まれています。

%description devel -l ko.UTF-8
이 패키지는 PCI 버스에 접속된 장치들을 조사하고 세팅하는데 사용되는
라이브러리를 포함하고 있습니다.

%description devel -l pl.UTF-8
Pakiet ten zawiera bibliotekę służącą do badania i konfigurowania
urządzeń przyłączonych do magistrali PCI.

%description devel -l pt.UTF-8
Este pacote contém uma biblioteca para inspeccionar e configurar
dispositivos ligados ao bus PCI.

%description devel -l pt_BR.UTF-8
Biblioteca de desenvolvimentos para aplicações que trabalhem com o
barramento PCI no Linux.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и другие файлы для разработки программ
инспектирующих и конфигурирующих устройства, подключенные к шине PCI.

%description devel -l sk.UTF-8
Tento balík obsahuje knižnicu pre prehliadanie a nastavovanie
zariadení pripojených na PCI zbernicu.

%description devel -l sv.UTF-8
Detta paket innehåller ett bibliotek för att inspektera och ställa in
enheter kopplade till PCI-bussen.

%description devel -l uk.UTF-8
Цей пакет містить хедери та інші файли для розробки програм,що
інспектують та конфігурують пристрої, під'єднані до шини PCI.

%description devel -l zh_CN.UTF-8
此软件包包含一个程序库，用于检查和设置与 PCI 总线连接的设备。

%package static
Summary:	Static version of PCI library
Summary(pl.UTF-8):	Statyczna wersja biblioteki PCI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of PCI library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki PCI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# paranoid check whether pci.ids in _sourcedir isn't too old
if [ $(wc -l < %{SOURCE2}) -lt $(wc -l < pci.ids) ] ; then
	: pci.ids needs to be updated
	exit 1
fi
cp -f %{SOURCE2} .

ln -sf lib pci

%build
%define	config	ZLIB=yes DNS=yes SHARED=yes

%{__make} lib/libpci.a \
	ZLIB=yes DNS=yes SHARED=no \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	PREFIX=%{_prefix} \
	IDSDIR=%{_datadir} \
	INCDIR=%{_includedir} \
	LIBDIR=%{_libdir}

rm -f lib/*.o lib/config.h lib/config.mk

%{__make} \
	%{config} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix} \
	IDSDIR=%{_datadir} \
	INCDIR=%{_includedir} \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-lib \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	SBINDIR=%{_sbindir} \
	SHAREDIR=%{_datadir} \
	PCI_IDS=pci.ids

install -d $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/libpci.so.* $RPM_BUILD_ROOT/%{_lib}
# let rpm find deps
chmod 755 $RPM_BUILD_ROOT/%{_lib}/libpci.so.*
ln -sf $(basename $RPM_BUILD_ROOT/%{_lib}/libpci.so.*.*.*) $RPM_BUILD_ROOT/%{_lib}/libpci.so.3
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libpci.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpci.so

install lib/libpci.a $RPM_BUILD_ROOT%{_libdir}

install pcimodules $RPM_BUILD_ROOT%{_sbindir}
# private pciutils header, what does it use?
install pciutils.h $RPM_BUILD_ROOT%{_includedir}/pci

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/{README.pciutils-non-english-man-pages,/pciutils-non_en_man.patch}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/lspci
%attr(755,root,root) %{_sbindir}/setpci
%attr(755,root,root) %{_sbindir}/pcimodules
%attr(755,root,root) %{_sbindir}/update-pciids
%attr(755,root,root) /%{_lib}/libpci.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpci.so.3
%{_datadir}/pci.ids
%{_mandir}/man7/pcilib.7*
%{_mandir}/man8/lspci.8*
%{_mandir}/man8/setpci.8*
%{_mandir}/man8/update-pciids.8*
%lang(ja) %{_mandir}/ja/man8/*
%lang(pl) %{_mandir}/pl/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpci.so
%dir %{_includedir}/pci
%{_includedir}/pci/*.h
%{_pkgconfigdir}/libpci.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpci.a
