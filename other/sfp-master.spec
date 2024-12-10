Name: sfp-master
Version: 1.0.1
Release: 1%dist

Summary: Reading, writing SFP modules data
Summary(ru_RU.UTF-8): Чтение, запись данных SFP-модулей
Summary(de_DE.UTF-8): Lesen und Schreiben von SFP-Modul-Daten
Summary(es_ES.UTF-8): Lectura, escritura de datos de módulos SFP
Summary(hu_HU.UTF-8): SFP modulok adatainak olvasása, írása
Summary(it_IT.UTF-8): Lettura e scrittura dei dati dei moduli SFP
Summary(pt_BR.UTF-8): Leitura e gravação de dados de módulos SFP
Summary(uk_UA.UTF-8): Читання, запис даних SFP модулів
Summary(zh_CN.UTF-8): 读取、写入 SFP 模块数据
License: GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only
Group: Applications/Engineering

Url: https://github.com/bigbigmdm/SFP-Master
Source: https://github.com/bigbigmdm/SFP-Master/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
SFP-Master is a free software programmer of optical SFP modules for CH341a 
devices. It can be used to read, write and save SFP module data to the computer.
It requires an SFP to I2C adapter. This adapter is used to read and program 
SFP-module data. It must be inserted into the slot labelled 24xxx of the CH341a
programmer.

%description -l ru_RU.UTF-8
SFP-Master - это бесплатный программатор оптических SFP-модулей для устройств 
CH341a. С его помощью можно считывать, записывать и сохранять данные SFP-модуля 
на компьютере. Для работы требуется адаптер SFP в I2C. Этот адаптер используется
для чтения и программирования данных SFP-модуля. Он должен быть вставлен в слот 
с маркировкой 24xxx программатора CH341a.

%description -l de_DE.UTF-8
SFP-Master ist ein kostenloses Programmier für optische SFP-Module für
CH341a-Geräte. Es kann zum Lesen, Schreiben und Speichern von SFP-Modul-Daten 
auf dem Computer verwendet werden. Es erfordert einen SFP-zu-I2C-Adapter. 
Dieser Adapter wird zum Lesen und Programmieren von SFP-Moduldaten verwendet. 
Er muss in den mit 24xxx gekennzeichneten Steckplatz des 
CH341a-Programmiergeräts eingesetzt werden.

%description -l es_ES.UTF-8
SFP-Master es un programador de software gratuito de módulos ópticos SFP para 
dispositivos CH341a. Se puede utilizar para leer, escribir y guardar datos del
módulo SFP en el ordenador. Requiere un adaptador SFP a I2C. Este adaptador se
utiliza para leer y programar los datos del módulo SFP. Debe insertarse en la
ranura etiquetada 24xxx del programador CH341a.

%description -l hu_HU.UTF-8
Az SFP-Master a CH341a eszközök optikai SFP moduljainak ingyenes szoftveres
programozója. Az SFP-modul adatainak olvasására, írására és számítógépre 
mentésére használható. Ehhez SFP-I2C adapterre van szükség. Ez az adapter az
SFP-modul adatainak olvasására és programozására szolgál. A CH341a programozó
24xxx feliratú nyílásába kell behelyezni.

%description -l it_IT.UTF-8
SFP-Master è un programmatore software gratuito di moduli ottici SFP per
dispositivi CH341a. Può essere utilizzato per leggere, scrivere e salvare i dati
del modulo SFP sul computer. Richiede un adattatore SFP-I2C. Questo adattatore
viene utilizzato per leggere e programmare i dati del modulo SFP. Deve essere
inserito nello slot 24xxx del programmatore CH341a.

%description -l pt_BR.UTF-8
O SFP-Master é um programador de software gratuito de módulos SFP ópticos para
dispositivos CH341a. Ele pode ser usado para ler, gravar e salvar dados do 
módulo SFP no computador. Ele requer um adaptador SFP para I2C. Esse adaptador
é usado para ler e programar os dados do módulo SFP. Ele deve ser inserido no
slot rotulado como 24xxx do programador CH341a.

%description -l uk_UA.UTF-8
SFP-Master - це безкоштовне програмне забезпечення для програмування оптичних 
SFP-модулів для пристроїв CH341a. Він може бути використаний для читання, запису
та збереження даних SFP-модуля на комп'ютері. Для роботи потрібен адаптер SFP до
I2C. Цей адаптер використовується для зчитування і програмування даних 
SFP-модуля. Його потрібно вставити в гніздо з маркуванням 24xxx програматора 
CH341a.

%description -l zh_CN.UTF-8
SFP-Master 是用于 CH341a 设备的光学 SFP 模块的免费编程软件。它可用于读写 SFP 模块数据并将其保存到计算机中。它需要一个 SFP 至 I2C 适配器。该适配器用于读取和编程 SFP 模块数据。它必须插入 CH341a 编程器标有 24xxx 的插槽中。

%prep
%autosetup -p1 -n IMSProg-%{version}

%build
# update translations
lrelease-qt5 language/*.ts

pushd SFP-Master
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build
popd

%install
pushd SFP-Master
%cmake_install
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%doc README.md 
%_docdir/sfp-master/
%_bindir/SFP-Master
%_datadir/applications/SFP-Master.desktop
%_datadir/metainfo/*.xml
/usr/lib/udev/rules.d/*.rules
%_datadir/pixmaps/.png
%_datadir/pixmaps/SFP-Master.png
%_datadir/man/man1/*.1.*
%license LICENSE

%changelog
* Wed Dec 10 2024 Mikhail Medvedev 1.0.1-1
- initial release