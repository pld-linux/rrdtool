#
# Conditional build:
%bcond_without	python	# Python binding
%bcond_without	tcl	# Tcl binding
%bcond_without	ruby	# Ruby binding
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	RRDp
Summary:	RRDtool - round robin database
Summary(pl.UTF-8):	RRDtool - baza danych typu round-robin
Summary(pt_BR.UTF-8):	Round Robin Database, uma ferramenta para construção de gráficos
Summary(ru.UTF-8):	RRDtool - база данных с "циклическим обновлением"
Summary(uk.UTF-8):	RRDtool - це система зберігання та показу серійних даних
Name:		rrdtool
Version:	1.4.5
Release:	2
License:	GPL v2+ + FLOSS exception
Group:		Applications/Databases
Source0:	http://oss.oetiker.ch/rrdtool/pub/%{name}-%{version}.tar.gz
# Source0-md5:	4d116dba9a0888d8aaac179e35d3980a
Patch0:		%{name}-tcl-path.patch
URL:		http://oss.oetiker.ch/rrdtool/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.6
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	glib2-devel >= 1:2.12.12
BuildRequires:	intltool
BuildRequires:	libdbi-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.31
BuildRequires:	lua51 >= 5.1
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pango-devel >= 1:1.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
%if %{with python}
BuildRequires:	python >= 2.3
BuildRequires:	python-devel >= 2.3
%endif
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.272
%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_tcl:BuildRequires:	tcl-devel}
Requires:	cairo >= 1.4.6
Requires:	glib2 >= 1:2.12.12
Requires:	libxml2 >= 2.6.31
Requires:	pango >= 1:1.17
Suggests:	fonts-TTF-DejaVu
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
Requires:	cairo-devel >= 1.4.6
Requires:	glib2-devel >= 1:2.12.12
Requires:	libdbi-devel
Requires:	libxml2-devel >= 2.6.31
Requires:	pango-devel >= 1:1.17

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

%package -n lua-rrdtool
Summary:	RRD module for Lua
Summary(pl.UTF-8):	Moduł RRD dla języka Lua
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	lua51

%description -n lua-rrdtool
Lua interface to RRDtool.

%description -n lua-rrdtool -l pl.UTF-8
Interfejs języka Lua do RRDtoola.

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

%package -n ruby-rrdtool
Summary:	Ruby interface to RRDtool
Summary(pl.UTF-8):	Interfejs języka Ruby do RRDtoola
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description -n ruby-rrdtool
Ruby interface to RRDtool, the graphing and logging utility.

%description -n ruby-rrdtool -l pl.UTF-8
Interfejs języka Ruby do RRDtoola - narzędzia do tworzenia wykresów i
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

sed -i -e 's#\$TCL_PACKAGE_PATH#%{_prefix}/lib#g' configure.ac
sed -i -e 's#/lib/lua/#/%{_lib}/lua/#g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LUA=/usr/bin/lua51 \
	--disable-silent-rules \
	%{!?with_tcl:--disable-tcl} \
	%{!?with_ruby:--disable-ruby} \
	--with-perl-options="INSTALLDIRS=vendor"

# empty RUBY_MAKE_OPTIONS as workaround for some make weirdness
# (tried to install without DESTDIR on plain make)
%{__make} \
	RUBY_MAKE_OPTIONS= \
	LUA_CFLAGS=-I/usr/include/lua51

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch} \
	pythondir=%{py_sitedir} \
	examplesdir=%{_examplesdir}/%{name}-%{version} \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lua/5.1/*.{la,a}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RRDs/.packlist

%{__rm} $RPM_BUILD_ROOT%{_libdir}/librrd.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS NEWS README THREADS TODO doc/*.html
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_libdir}/librrd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librrd.so.4
%attr(755,root,root) %{_libdir}/librrd_th.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librrd_th.so.4
%{_mandir}/man1/bin_dec_hex.1*
%{_mandir}/man1/cdeftutorial.1*
%{_mandir}/man1/rpntutorial.1*
%{_mandir}/man1/rrd*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librrd.so
%attr(755,root,root) %{_libdir}/librrd_th.so
%{_libdir}/librrd_th.la
%{_includedir}/rrd*.h
%{_pkgconfigdir}/librrd.pc
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/librrd.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a
%{_libdir}/librrd_th.a

%files -n lua-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/5.1/rrd.so*

%files -n perl-rrdtool
%defattr(644,root,root,755)
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%dir %{perl_vendorarch}/auto/RRDs
%{perl_vendorarch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man3/RRDp.3*
%{_mandir}/man3/RRDs.3*

%if %{with python}
%files -n python-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/rrdtoolmodule.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/py_rrdtool-*.egg-info
%endif
%endif

%if %{with ruby}
%files -n ruby-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/RRD.so
%endif

%if %{with tcl}
%files -n tcl-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclrrd%{version}.so
%{_prefix}/lib/tclrrd%{version}
%endif
