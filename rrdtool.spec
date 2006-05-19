%include	/usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pl):	RRDtool - baza danych typu round-robin
Summary(pt_BR):	Round Robin Database, uma ferramenta para construГЦo de grАficos
Summary(ru):	RRDtool - база данных с "циклическим обновлением"
Summary(uk):	RRDtool - це система збер╕гання та показу сер╕йних даних
Name:		rrdtool
Version:	1.2.12
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/%{name}-%{version}.tar.gz
# Source0-md5:	7b544c38a818cbebcf06fe39b9f52d0d
Patch0:		%{name}-tcl-path.patch
URL:		http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.7
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel >= 1.2.1
Requires:	libart_lgpl >= 2.3.17
Requires:	libpng >= 1.2.8
Requires:	zlib >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store
and display time-series data (i.e. network bandwidth, machine-room
temperature, server load average). It stores the data in a very
compact way that will not expand over time, and it presents useful
graphs by processing the data to enforce a certain data density. It
can be used either via simple wrapper scripts (from shell or Perl) or
via frontends that poll network devices and put a friendly user
interface on it.

%description -l pl
RRD jest akronimem Round Robin Database. Jest to system pozwalaj╠cy na
skЁadowanie i wy╤wietlanie czasowych serii danych (np. przepustowo╤Ф
sieci, temperatura w pomieszczeniu, obci╠©enie serwera). SkЁaduje dane
w "skondensowanej" postaci, ktСra nie rozrasta siЙ z biegiem czasu
oraz pozwala na produkowanie wykresСw z u©ytecznymi danymi. Mo©e byФ
u©ywane poprzez prosty skrypcik (shell lub perl), frontendy czy inne
interfejsy u©ytkownika.

%description -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaГЦo de rede, temperaturas, cargas em servidores).
Os dados sЦo armazenados em uma forma compacta que nЦo se expande com
o tempo, e grАficos podem ser apresentados processando-se esses dados.
RRD pode ser utilizado com wrapper scripts (em shell ou Perl) ou
atravИs de front-ends.

%description -l ru
RRD - соращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определенный промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера). Она
сохраняет данные в очень компактной форме, так что данные не будут
занимать все больше и больше места с течением времени и предоставляет
разумное графическое представление информации. Может быть использована
как из простых скриптов (shell, perl, etc) или встроена в программы,
которые опрашивают сетевые устройства и показывают данные в удобном
для пользователя виде.

%description -l uk
Назва RRD - це акрон╕м для Round Robin Database. RRD - це система
збер╕гання та показу сер╕йних даних (наприклад, полоси каналу,
температура гермозони, завантаження сервера). RRD збер╕га╓ дан╕ дуже
компактно ╕ так, що розм╕р бази даних не зб╕льшу╓ться з часом, та
презенту╓ корисн╕ граф╕ки обробляючи дан╕ з тим, щоб встановити
потр╕бну щ╕льн╕сть виб╕рки в час╕. RRD можна використовувати як через
прост╕ wrapper-скрипти, так ╕ через фронтенди, що опитують мережев╕
пристро╖ та надають дружн╕й ╕нтерфейс користувача.

%package devel
Summary:	RRDtool development
Summary(pl):	NarzЙdzia programistyczne pakietu RRDtool
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo da librrd
Summary(ru):	RRDtool - Заголовки, необходимые для разработки
Summary(uk):	RRDtool - б╕бл╕отечн╕ л╕нки та файли хедер╕в
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cgilibc-devel >= 0.5
Requires:	freetype-devel >= 2.1.7
Requires:	libart_lgpl-devel >= 2.3.17
Requires:	libpng-devel >= 2:1.2.8
Requires:	zlib-devel >= 1.2.1

%description devel
RRDtool development files.

%description devel -l pl
NarzЙdzia programistyczne pakietu RRDtool.

%description devel -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaГЦo de rede, temperaturas, cargas em servidores).

Este pacote contem arquivos de desenvolvimento do RRD.

%description devel -l ru
RRD - соращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определенный промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера).

Этот пакет позволяет создавать программы, которые используют это
библиотеку непосредственно.

%description devel -l uk
RRDtool - библиотечные линки и файлы хедеров.

%package static
Summary:	RRDtool static library
Summary(pl):	Statyczne biblioteki RRDtool
Summary(pt_BR):	Biblioteca estАtica librrd
Summary(ru):	RRDtool - Статические библиотеки
Summary(uk):	Статичн╕ б╕бл╕отеки RRDtool
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
RRDtool static library.

%description static -l pl
Statyczne biblioteki RRDtool.

%description static -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaГЦo de rede, temperaturas, cargas em servidores).

Este pacote contem a biblioteca estАtica do RRD.

%description static -l ru
RRD - соращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определенный промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера). Этот
пакет позволяет создавать статически слинкованные программы, которые
используют это библиотеку непосредственно.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм, що використовують RRDtool.

%package -n perl-rrdtool
Summary:	Access RRDtool from Perl
Summary(pl):	DostЙp do RRDtoola z poziomu Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-rrdtool
Perl modules to access RRDtool: RRDs to access RRDtool as shared
module and RRDp to access RRDtool via a set of pipes.

%description -n perl-rrdtool -l pl
ModuЁy Perla pozwalaj╠ce na dostЙp do RRDtoola: RRDs do dostЙpu do
RRDtoola jako moduЁu dzielonego oraz RRDp do dostЙpu poprzez zestaw
potokСw.

%package -n python-rrdtool
Summary:	Python interface to RRDtool
Summary(pl):	Pythonowy interfejs do RRDtoola
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-rrdtool
Python interface to RRDtool, the graphing and logging utility.

%description -n python-rrdtool -l pl
Interfejs Pythona do RRDtoola - narzЙdzia do tworzenia wykresСw i
logowania.

%package -n tcl-rrdtool
Summary:	Tcl extension to access the RRD library
Summary(pl):	Rozszerzenie Tcl-a pozwalaj╠ce na dostЙp do biblioteki Tcl
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl

%description -n tcl-rrdtool
Tcl extension to access the RRD library.

%description -n tcl-rrdtool -l pl
Rozszerzenie Tcl-a pozwalaj╠ce na dostЙp do biblioteki Tcl.

%prep
%setup -q
%patch0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-latin2 \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch} \
	pythondir=%{py_sitedir} \
	examplesdir=%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_prefix}/{doc,html}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS NEWS README THREADS TODO doc/*.html
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_libdir}/librrd.so.*.*.*
%attr(755,root,root) %{_libdir}/librrd_th.so.*.*.*
%{_datadir}/rrdtool
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librrd.so
%attr(644,root,root) %{_libdir}/librrd_th.so
%{_libdir}/librrd.la
%{_libdir}/librrd_th.la
%{_includedir}/rrd.h
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a
%{_libdir}/librrd_th.a

%files -n perl-rrdtool
%defattr(644,root,root,755)
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%dir %{perl_vendorarch}/auto/RRDs
%{perl_vendorarch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man3/RRDp.3*
%{_mandir}/man3/RRDs.3*

%files -n python-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/rrdtoolmodule.so

%files -n tcl-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclrrd%{version}.so
/usr/lib/tclrrd%{version}
