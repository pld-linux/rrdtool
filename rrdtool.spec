%include        /usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pl):	RRDtool - baza danych typu round-robin
Summary(pt_BR):	Round Robin Database, uma ferramenta para construГЦo de grАficos
Summary(ru):	RRDtool - база данных с "циклическим обновлением"
Summary(uk):	RRDtool - це система збер╕гання та показу сер╕йних даних
Name:		rrdtool
Version:	1.0.35
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://ee-staff.ethz.ch/~oetiker/webtools/rrdtools/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-perl-install.patch
URL:		http://ee-staff.ethz.ch/~oetiker/webtools/rrdtol/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-devel >= 5.6.1
#BuildRequired:	tcl-devel
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
sieci, temperatura w pomieszczeniu, obci╠©enie servera). SkЁaduje dane
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
Summary:	RDDTools development
Summary(pl):	NarzЙdzia programistyczne pakietu RRDtools
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo da librrd
Summary(ru):	RRDtool - база данных с "циклическим обновлением".  Заголовки, необходимые для разработки
Summary(uk):	RRDtool - б╕бл╕отечн╕ л╕нки та файли хедер╕в
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
RDDTools development files.

%description devel -l pl
NarzЙdzia programistyczne pakietu RRDtools.

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

%description devel -l ru
RRDtool - библиотечные линки и файлы хедеров.

%package static
Summary:	RDDTools static library
Summary(pl):	Statyczne biblioteki RRDtools
Summary(pt_BR):	Biblioteca estАtica librrd
Summary(ru):	RRDtool - база данных с "циклическим обновлением". Статические библиотеки
Summary(uk):	Статичн╕ б╕бл╕отеки RRDtool
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
RDDTools static library.

%description static -l pl
Statyczne biblioteki RRDtools.

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure \
	--enable-shared=yes \
	--without-tclib
# uncoment this line ONLY IF tcl package is ready.
#	--with-tclib=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_sitearch}

%{__make} site-perl-install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_sitearch}

(cd $RPM_BUILD_ROOT%{_examplesdir}/%{name};
mv -f ../../../examples/* .;
mv -f ../../../contrib .)

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_bindir}/trytime
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{perl_sitearch}/*.pm
%dir %{perl_sitearch}/auto/RRDs
%{perl_sitearch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_sitearch}/auto/RRDs/RRDs.so
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librrd.so
%attr(644,root,root) %{_libdir}/librrd.la
%{_examplesdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a
