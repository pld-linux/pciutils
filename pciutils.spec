Summary:	Linux PCI utilities
Summary(cs):	Linuxové utility pro PCI
Summary(da):	PCI-bus-relaterede værktøjer
Summary(de):	PCI-Bus verwandte Dienstprogramme
Summary(es):	Utilitarios Linux para PCI
Summary(fr):	Utilitaires relatifs au bus PCI
Summary(it):	Utility correlate al bus PCI
Summary(ja):	PCI ¥Ğ¥¹´ØÏ¢¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(ko):	PCI ¹ö½º °ü·Ã À¯Æ¿¸®Æ¼µé
Summary(nb):	PCI-buss-relaterte verktøy
Summary(pl):	Narzêdzia do manipulacji ustawieniami urz±dzeñ PCI
Summary(pt):	Utilitários relacionados com o 'bus' PCI
Summary(pt_BR):	Utilitários para PCI do Linux
Summary(ru):	õÔÉÌÉÔÙ ÒÁÂÏÔÙ Ó PCI ÕÓÔÒÏÊÓÔ×ÁÍÉ
Summary(sv):	PCI-bussrelaterade verktyg
Summary(uk):	õÔÉÌ¦ÔÉ ÒÏÂÏÔÉ Ú PCI ĞÒÉÓÔÒÏÑÍÉ
Summary(zh_CN):	PCI ×ÜÏßÏà¹ØµÄ¹¤¾ß¡£
Name:		pciutils
Version:	2.1.11
Release:	9
License:	GPL
Group:		Applications/System
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
# Source0-md5:	1d40f90aaae69594790bdb8ff90b4a41
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/pciutils-non-english-man-pages.tar.bz2
# Source1-md5:	1ac48f433b1995044e14c24513992211
Source2:	http://pciids.sourceforge.net/pci.ids
# NoSource2-md5:	3db20d38b4d78f46ee9c478293a75350
Patch0:		%{name}-bufsiz.patch
Patch1:		%{name}-devel.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-segv.patch
Patch4:		%{name}-pci_h.patch
Patch5:		%{name}-pcimodules.patch
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_libdir		%{_prefix}/%{_lib}
%define		_datadir	/etc

%description
This package contains various utilities for inspecting and setting of
devices connected to the PCI bus. Requires kernel version 2.1.82 or
newer (supporting the /proc/bus/pci interface).

%description -l cs
Balíèek pciutils obsahuje rùzné programy pro prohlí¾ení a nastavování
zaøízení pøipojenıch na sbìrnici PCI. Obsa¾ené programy vy¾adují jádro
verze 2.1.82 nebo novìj¹í (podporující rozhraní /proc/bus/pci).

%description -l da
Pakken pciutils indeholder forskellige værktøjer for at undresøge og
opsætte enheder koplet til PCI-bussen. Værktøjet kræver kerneversion
2.1.82 eller senere (som understøtter grænsefladen /proc/bus/pci).

%description -l de
Das pciutils Paket enthält verschiedene Dienstprogramme für das
Überprüfen und Konfigurieren von Geräten, die an den PCI-Bus
angeschlossen sind. Die bereitgestellten Dienstprogramme erfordern
Kernel Version 2.1.82 oder neuer (und die darin implementierte
Unterstützung der Schnittstelle /proc/bus/pci).

%description -l es
Este paquete contiene varias utilidades para controlar y configurar
los dispositivos conectados al bus PCI. Las utilidades ofrecidas en
este paquete requieren la versión 2.1.82 o una posterior del kernel
(necesita del soporte para la interfaz /proc/bus/pci).

%description -l fr
Le paquetage pciutils contient divers utilitaires permettant
d'inspecter et de paramétrer des périphériques connectés au bus PCI.
Les utilitaires fournis requièrent un noyau version 2.1.82 ou plus
récent (prenant en charge l'interface /proc/bus/pci).

%description -l id
Paket ini berisi berbagai utilitas untuk mengamati dan mengeset device
yang terhubung ke bus PCI. Utilitas yang disediakan ini membutuhkan
kernel versi 2.1.82 atau yang lebih baru (yaitu yang mendukung
antarmuka /proc/bus/pci).

%description -l is
Şessi pakki inniheldur ımis tól til ağ skoğa og setja tæki tengd PCI
rútunni. Tólin eru nauğsynleg fyrir kjarna 2.1.82 eğa nırri (styğja
/proc/bus/pci viğmótiğ).

%description -l it
Il pacchetto pciutils contiene varie utility per controllare e
configurare i dispositivi collegati al bus PCI. L'utility fornita in
questo pacchetto richiede la versione 2.1.82 o successiva del kernel
(richiede il supporto per l'interfaccia /proc/bus/pci).

%description -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï¡¢PCI ¥Ğ¥¹¤ËÀÜÂ³¤µ¤ì¤¿¥Ç¥Ğ¥¤¥¹¤òÄ´ºº¡¢ÀßÄê¤¹¤ë¤¿
¤á¤Î³Æ¼ï¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤¬´Ş¤Ş¤ì¤Æ¤¤¤Ş¤¹¡£¤½¤ì¤é¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï¡¢¥«¡¼
¥Í¥ë¥Ğ¡¼¥¸¥ç¥ó 2.1.82 °Ê¹ß (/proc/bus/pci ¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤ò¥µ¥İ¡¼¥È)
¤òÉ¬Í×¤È¤·¤Ş¤¹¡£

%description -l pl
Pakiet zawiera narzêdzia do ustawiania i odczytywania informacji o
urz±dzeniach pod³±czonych do szyny PCI w Twoim komputerze. Wymaga
kernela 2.1.82 lub nowszego (udostêpniaj±cego odpowiednie informacje
poprzez /proc/bus/pci).

%description -l pt
Este pacote contém vários utilitários para inspeccionar e configurar
os dispositivos ligados ao bus PCI. Os utilitários fornecidos precisam
dum núcleo ou 'kernel' versão 2.1.82 ou mais recente (que suporte a
interface /proc/bus/pci).

%description -l pt_BR
Este pacote contém vários utilitários para inspeção e configuração de
dispositivos conectados ao barramento PCI do seu computador.

%description -l ru
ğÁËÅÔ ÓÏÄÅÒÖÉÔ ÒÁÚÌÉŞÎÙÅ ÕÔÉÌÉÔÙ ÄÌÑ ĞÒÏ×ÅÒËÉ É ÎÁÓÔÒÏÊËÉ ÕÓÔÒÏÊÓÔ×,
ĞÏÄËÌÀŞÅÎÎÙÈ Ë ÛÉÎÅ PCI. õÔÉÌÉÔÁ ÔÒÅÂÕÅÔ ÑÄÒÏ ×ÅÒÓÉÉ 2.1.82 (ÉÌÉ ÂÏÌÅÅ
ÎÏ×ÏÊ ×ÅÒÓÉÉ), ĞÏÄÄÅÒÖÉ×ÁÀÅÊ ÉÎÔÅÒÆÅÊÓ /proc/bus/pci.

%description -l sk
Tento balík obsahuje rozlièné pomocné programy pre prehliadanie a
nastavovanie zariadení pripojenıch na PCI zbernicu. Nástroje vy¾adujú
jadro s èíslom verzie aspoò 2.1.82 (podporujúce rozhranie
/proc/bus/pci).

%description -l sv
Paketet pciutils innehåller olika verktyg för att inspektera och
ställa in enheter kopplade till PCI-bussen. Verktygen kräver
kärnversion 2.1.82 eller senare (som stödjer gränssnittet
/proc/bus/pci).

%description -l uk
ğÁËÅÔ pciutils Í¦ÓÔÉÔØ ÕÔÉÌ¦ÔÉ ÄÌÑ ¦ÎÓĞÅËÔÕ×ÁÎÎÑ ÔÁ ËÏÎÆ¦ÇÕÒÕ×ÁÎÎÑ
ĞÒÉÓÔÒÏ§×, Ğ¦Ä'¤ÄÎÁÎÉÈ ÄÏ PCI ÛÉÎÉ. äÌÑ ÒÏÂÏÔÉ Ã¦ ÕÔÉÌ¦ÔÉ ĞÏÔÒÅÂÕÀÔØ
ÎÁÑ×ÎÏÓÔ¦ ¦ÎÔÅÒÆÅÊÓÕ /proc/bus/pci.

%package devel
Summary:	Linux PCI development library
Summary(cs):	Linuxová vıvojová knihovna pro PCI
Summary(da):	Linux PCI udviklingsbibliotek
Summary(de):	Linux PCI-Entwicklungsbibliothek
Summary(es):	Biblioteca de desarrollo para aplicaciones que trabajan con el bus PCI en Linux
Summary(fr):	Bibliothèque de développement PCI Linux
Summary(id):	Library pengembangan PCI Linux
Summary(is):	PCI şróunarağgerğasafn fyrir Linux
Summary(it):	Libreria di sviluppo PCI per Linux
Summary(ja):	Linux PCI ³«È¯¥é¥¤¥Ö¥é¥ê
Summary(ko):	Linux PCI °³¹ß¿ë ¶óÀÌºê·¯¸®
Summary(nb):	Linux PCI utviklingsbibliotek
Summary(pl):	Pliki developerskie pciutils
Summary(pt):	Biblioteca de desenvolvimento para PCI do Linux
Summary(pt_BR):	Biblioteca de desenvolvimentos para aplicações que trabalhem com o barramento PCI no Linux
Summary(ru):	èÅÄÅÒÙ É ÄÒÕÇÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÏÇÒÁÍÍ, ÒÁÂÏÔÁÀİÉÈ Ó ÛÉÎÏÊ PCI
Summary(sk):	Kni¾nica pre vıvoj PCI na Linuxe
Summary(sl):	Razvojna knji¾nica za PCI v Linuxu
Summary(sv):	Linux PCI utvecklignsbibliotek
Summary(uk):	èÅÄÅÒÉ ÔÁ ¦ÎÛ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ĞÒÏÇÒÁÍ, İÏ ĞÒÁÃÀÀÔØ Ú ÛÉÎÏÀ PCI
Summary(zh_CN):	Linux PCI ¿ª·¢³ÌĞò¿â¡£
Group:		Development/Libraries

%description devel
This package contains a library for inspecting and setting devices
connected to the PCI bus.

%description devel -l cs
Tento balíèek obsahuje knihovny pro prohlí¾ení a nastavování zaøízení
pøipojenıch k PCI sbìrnici.

%description devel -l da
Denne pakke indeholder et bibliotek for at inspektere og stælla in
enheder kopplade til PCI-bussen.

%description devel -l de
Dieses Paket enthält eine Bibliothek für das Überprüfen und
Konfigurieren von Geräten, die an den PCI-Bus angeschlossen sind.

%description devel -l es
Biblioteca de desarrollo para aplicaciones que trabajen con el bus PCI
en Linux.

%description devel -l fr
Ce paquetage contient une bibliothèque permettant d'inspecter et de
définir des périphériques connectés au bus PCI.

%description devel -l id
Paket ini berisi library untuk mengamati dan mengeset device yang
terhubung ke bus PCI.

%description devel -l is
Şessi pakki inniheldur ağgerğasafn til ağ skoğa og setja tæki tengd
PCI rútunni.

%description devel -l it
Questo pacchetto contiene una libreria per controllare e configurare i
dispositivi collegati al bus PCI.

%description devel -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï¡¢PCI ¥Ğ¥¹¤ËÀÜÂ³¤µ¤ì¤¿¥Ç¥Ğ¥¤¥¹¤ò¸¡ºº¡¢ÀßÄê
¤¹¤ë¤¿¤á¤Î¥é¥¤¥Ö¥é¥ê¤¬´Ş¤Ş¤ì¤Æ¤¤¤Ş¤¹¡£

%description devel -l ko
ÀÌ ÆĞÅ°Áö´Â PCI ¹ö½º¿¡ Á¢¼ÓµÈ ÀåÄ¡µéÀ» Á¶»çÇÏ°í ¼¼ÆÃÇÏ´Âµ¥ »ç¿ëµÇ´Â
¶óÀÌºê·¯¸®¸¦ Æ÷ÇÔÇÏ°í ÀÖ½À´Ï´Ù.

%description devel -l pl
Pakiet ten zawiera bibliotekê s³u¿±c± do badania i konfigurowania
urz±dzeñ przy³±czonych do magistrali PCI.

%description devel -l pt
Este pacote contém uma biblioteca para inspeccionar e configurar
dispositivos ligados ao bus PCI.

%description devel -l pt_BR
Biblioteca de desenvolvimentos para aplicações que trabalhem com o
barramento PCI no Linux.

%description devel -l ru
üÔÏÔ ĞÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ É ÄÒÕÇÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ĞÒÏÇÒÁÍÍ
ÉÎÓĞÅËÔÉÒÕÀİÉÈ É ËÏÎÆÉÇÕÒÉÒÕÀİÉÈ ÕÓÔÒÏÊÓÔ×Á, ĞÏÄËÌÀŞÅÎÎÙÅ Ë ÛÉÎÅ PCI.

%description devel -l sk
Tento balík obsahuje kni¾nicu pre prehliadanie a nastavovanie
zariadení pripojenıch na PCI zbernicu.

%description devel -l sv
Detta paket innehåller ett bibliotek för att inspektera och ställa in
enheter kopplade till PCI-bussen.

%description devel -l uk
ãÅÊ ĞÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÔÁ ¦ÎÛ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ĞÒÏÇÒÁÍ,İÏ
¦ÎÓĞÅËÔÕÀÔØ ÔÁ ËÏÎÆ¦ÇÕÒÕÀÔØ ĞÒÉÓÔÒÏ§, Ğ¦Ä'¤ÄÎÁÎ¦ ÄÏ ÛÉÎÉ PCI.

%description devel -l zh_CN
´ËÈí¼ş°ü°üº¬Ò»¸ö³ÌĞò¿â£¬ÓÃÓÚ¼ì²éºÍÉèÖÃÓë PCI ×ÜÏßÁ¬½ÓµÄÉè±¸¡£

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# paranoid check whether pci.ids in _sourcedir isn't too old
if [ "`wc -l < %{SOURCE2}`" -lt "`wc -l < pci.ids`" ] ; then
	echo "pci.ids needs to be updated"
	exit 1
fi
cp -f %{SOURCE2} .

cp -rf lib pci

%build
%{__make} lib/config.h pci/config.h \
	SHAREDIR=%{_datadir}

%{__make} -C lib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	SHAREDIR=/etc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir},%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci pcimodules	$RPM_BUILD_ROOT%{_sbindir}
install *.h lib/[ch]*.h	$RPM_BUILD_ROOT%{_includedir}/pci
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install pci.ids		$RPM_BUILD_ROOT%{_datadir}
install lib/libpci.a	$RPM_BUILD_ROOT%{_libdir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
cp -f lib/pci.h		$RPM_BUILD_ROOT%{_includedir}/pci

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
