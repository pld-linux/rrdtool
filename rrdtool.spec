%include	/usr/lib/rpm/macros.perl
%define	pdir	RRDp
Summary:	RRDtool - round robin database
Summary(pl.UTF-8):	RRDtool - baza danych typu round-robin
Summary(pt_BR.UTF-8):	Round Robin Database, uma ferramenta para construção de gráficos
Summary(ru.UTF-8):	RRDtool - база данных с "циклическим обновлением"
Summary(uk.UTF-8):	RRDtool - це система зберігання та показу серійних даних
Name:		rrdtool
Version:	1.2.26
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://oss.oetiker.ch/rrdtool/pub/%{name}-%{version}.tar.gz
# Source0-md5:	b2c179e2d2ec2a92969648c4ebd382dc
Patch0:		%{name}-tcl-path.patch
URL:		http://oss.oetiker.ch/rrdtool/	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.7
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
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

%description -l pl.UTF-8
RRD jest akronimem Round Robin Database. Jest to system pozwalający na
składowanie i wyświetlanie czasowych serii danych (np. przepustowość
sieci, temperatura w pomieszczeniu, obciążenie serwera). Składuje dane
w "skondensowanej" postaci, która nie rozrasta się z biegiem czasu
oraz pozwala na produkowanie wykresów z użytecznymi danymi. Może być
używane poprzez prosty skrypcik (shell lub perl), frontendy czy inne
interfejsy użytkownika.

%description -l pt_BR.UTF-8
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).
Os dados são armazenados em uma forma compacta que não se expande com
o tempo, e gráficos podem ser apresentados processando-se esses dados.
RRD pode ser utilizado com wrapper scripts (em shell ou Perl) ou
através de front-ends.

%description -l ru.UTF-8
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

%description -l uk.UTF-8
Назва RRD - це акронім для Round Robin Database. RRD - це система
зберігання та показу серійних даних (наприклад, полоси каналу,
температура гермозони, завантаження сервера). RRD зберігає дані дуже
компактно і так, що розмір бази даних не збільшується з часом, та
презентує корисні графіки обробляючи дані з тим, щоб встановити
потрібну щільність вибірки в часі. RRD можна використовувати як через
прості wrapper-скрипти, так і через фронтенди, що опитують мережеві
пристрої та надають дружній інтерфейс користувача.

%package devel
Summary:	RRDtool development
Summary(pl.UTF-8):	Narzędzia programistyczne pakietu RRDtool
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão da librrd
Summary(ru.UTF-8):	RRDtool - Заголовки, необходимые для разработки
Summary(uk.UTF-8):	RRDtool - бібліотечні лінки та файли хедерів
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cgilibc-devel >= 0.5
Requires:	freetype-devel >= 2.1.7
Requires:	libart_lgpl-devel >= 2.3.17
Requires:	libpng-devel >= 2:1.2.8
Requires:	zlib-devel >= 1.2.1

%description devel
RRDtool development files.

%description devel -l pl.UTF-8
Narzędzia programistyczne pakietu RRDtool.

%description devel -l pt_BR.UTF-8
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).

Este pacote contem arquivos de desenvolvimento do RRD.

%description devel -l ru.UTF-8
RRD - соращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определенный промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера).

Этот пакет позволяет создавать программы, которые используют это
библиотеку непосредственно.

%description devel -l uk.UTF-8
RRDtool - библиотечные линки и файлы хедеров.

%package static
Summary:	RRDtool static library
Summary(pl.UTF-8):	Statyczne biblioteki RRDtool
Summary(pt_BR.UTF-8):	Biblioteca estática librrd
Summary(ru.UTF-8):	RRDtool - Статические библиотеки
Summary(uk.UTF-8):	Статичні бібліотеки RRDtool
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
RRDtool static library.

%description static -l pl.UTF-8
Statyczne biblioteki RRDtool.

%description static -l pt_BR.UTF-8
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).

Este pacote contem a biblioteca estática do RRD.

%description static -l ru.UTF-8
RRD - соращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определенный промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера). Этот
пакет позволяет создавать статически слинкованные программы, которые
используют это библиотеку непосредственно.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм, що використовують RRDtool.

%package -n perl-rrdtool
Summary:	Access RRDtool from Perl
Summary(pl.UTF-8):	Dostęp do RRDtoola z poziomu Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-rrdtool
Perl modules to access RRDtool: RRDs to access RRDtool as shared
module and RRDp to access RRDtool via a set of pipes.

%description -n perl-rrdtool -l pl.UTF-8
Moduły Perla pozwalające na dostęp do RRDtoola: RRDs do dostępu do
RRDtoola jako modułu dzielonego oraz RRDp do dostępu poprzez zestaw
potoków.

%package -n python-rrdtool
Summary:	Python interface to RRDtool
Summary(pl.UTF-8):	Pythonowy interfejs do RRDtoola
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-rrdtool
Python interface to RRDtool, the graphing and logging utility.

%description -n python-rrdtool -l pl.UTF-8
Interfejs Pythona do RRDtoola - narzędzia do tworzenia wykresów i
logowania.

%package -n tcl-rrdtool
Summary:	Tcl extension to access the RRD library
Summary(pl.UTF-8):	Rozszerzenie Tcl-a pozwalające na dostęp do biblioteki Tcl
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl

%description -n tcl-rrdtool
Tcl extension to access the RRD library.

%description -n tcl-rrdtool -l pl.UTF-8
Rozszerzenie Tcl-a pozwalające na dostęp do biblioteki Tcl.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-latin2 \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor"

# empty RUBY_MAKE_OPTIONS as workaround for some make weirdness
# (tried to install without DESTDIR on plain make)
%{__make} \
	RUBY_MAKE_OPTIONS=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch} \
	pythondir=%{py_sitedir} \
	examplesdir=%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_prefix}/{doc,html}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/ntmake.pl
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RRDs/.packlist

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
%attr(755,root,root) %{_libdir}/librrd.so
%attr(755,root,root) %{_libdir}/librrd_th.so
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
%{py_sitedir}/py_rrdtool-*.egg-info

%files -n tcl-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclrrd%{version}.so
%{_prefix}/lib/tclrrd%{version}
