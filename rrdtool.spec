%include	/usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pl):	RRDtool - baza danych typu round-robin
Summary(pt_BR):	Round Robin Database, uma ferramenta para construГЦo de grАficos
Summary(ru):	RRDtool - база данных с "циклическим обновлением"
Summary(uk):	RRDtool - це система збер╕гання та показу сер╕йних даних
Name:		rrdtool
Version:	1.0.49
Release:	2
License:	GPL
Group:		Applications/Databases
Source0:	http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/%{name}-%{version}.tar.gz
# Source0-md5:	fbe492dbf3d68abb1d86c2322e7ed44a
Patch0:		%{name}-perl-install.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-system-libs.patch
Patch3:		%{name}-php-config.patch
Patch4:		%{name}-libdir.patch
URL:		http://ee-staff.ethz.ch/~oetiker/webtools/rrdtol/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cgilibc-devel
BuildRequires:	gd-devel >= 1.3
BuildRequires:	libpng-devel >= 1.0.9
BuildRequires:	libtool
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	php-devel
BuildRequires:	rpm-perlprov
BuildConflicts:	perl-devel = 1:5.8.2-1
#BuildRequired:	tcl-devel
BuildRequires:	zlib-devel >= 1.1.4
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
Summary:	RRDtool development
Summary(pl):	NarzЙdzia programistyczne pakietu RRDtool
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo da librrd
Summary(ru):	RRDtool - Заголовки, необходимые для разработки
Summary(uk):	RRDtool - б╕бл╕отечн╕ л╕нки та файли хедер╕в
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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

%package -n php-rrdtool
Summary:	RRDtool php module
Summary(pl):	ModuЁ PHP RRDtool
Group:		Unknown/Unknown
Requires(post,preun):	php-common
Requires:	php-common

%description -n php-rrdtool
RRDtool module for PHP.

%description -n php-rrdtool -l pl
ModuЁ RRDtool dla PHP.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0

%{__perl} -pi -e 's/--localdir=/-B /g' Makefile.am */Makefile.am

%build
rm -rf cgilib* libpng* zlib* gd*
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader} -I config
%{__automake}
CPPFLAGS="-I%{_includedir}/cgilibc"
%configure \
	--enable-shared=yes \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor" \
	--without-tclib
# uncoment this line ONLY IF tcl package is ready.
#	--with-tclib=%{_prefix}
%{__make} install \
	DESTDIR="$(pwd)/temp-install"
cd contrib/php4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-openssl \
	--with-rrdtool="$(pwd)/../../temp-install%{_prefix}" \
	--includedir="%{_includedir}/php"
%{__make}
cd ../../

# Fix @perl@ and @PERL@
find examples/ -type f \
	-exec /usr/bin/perl -pi -e 's|^#! \@perl\@|#!/usr/bin/perl|gi' "{}" ";"
find examples/ -name "*.pl" \
	-exec perl -pi -e 's|\015||gi' "{}" ";"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch}

# this shoudn't be required...
%{__make} site-perl-install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch}

install -m755 -D contrib/php4/modules/rrdtool.so $RPM_BUILD_ROOT%{_libdir}/php/rrdtool.so

cd $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv -f ../../../examples/* .
mv -f ../../../contrib .

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n php-rrdtool
%{_sbindir}/php-module-install install rrdtool %{_sysconfdir}/php.ini

%preun -n php-rrdtool
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove rrdtool %{_sysconfdir}/php.ini
fi

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README TODO doc/*.html
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_bindir}/trytime
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/RRDs
%{perl_vendorarch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librrd.so
%{_libdir}/librrd.la
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a

%files -n php-rrdtool
%defattr(644,root,root,755)
%doc contrib/php4/examples contrib/php4/README
%{_libdir}/php/rrdtool.so
