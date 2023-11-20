# TODO:
# - SysV init script for rrdcached, post/postun/etc.
#
# Conditional build:
%bcond_without	lua		# LUA binding
%bcond_without	perl		# Perl binding
%bcond_without	python		# Python binding
%bcond_without	ruby		# Ruby binding
%bcond_without	tcl		# Tcl binding
%bcond_without	ceph		# Ceph (RADOS) storage support
%bcond_without	rrd_graph	# all rrd_graph functions (depend on cairo+pango)
%bcond_without	rrdcgi		# building of rrdcgi (depends on rrd_graph)
%bcond_without	static_libs	# static library

%if %{without rrd_graph}
%undefine	with_rrdcgi
%endif

%define	pdir	RRDp
Summary:	RRDtool - round robin database
Summary(pl.UTF-8):	RRDtool - baza danych typu round-robin
Summary(pt_BR.UTF-8):	Round Robin Database, uma ferramenta para construção de gráficos
Summary(ru.UTF-8):	RRDtool - база данных с "циклическим обновлением"
Summary(uk.UTF-8):	RRDtool - це система зберігання та показу серійних даних
Name:		rrdtool
Version:	1.8.0
Release:	1
License:	GPL v2+ + FLOSS exception
Group:		Applications/Databases
Source0:	https://github.com/oetiker/rrdtool-1.x/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	852754364cbd0703a099b5eb32932851
Patch0:		%{name}-tcl-path.patch
Patch1:		%{name}-build.patch
URL:		http://oss.oetiker.ch/rrdtool/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_ceph:BuildRequires:	ceph-devel}
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.28.7
BuildRequires:	groff
BuildRequires:	libdbi-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxml2-devel >= 1:2.7.8
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with rrd_graph}
BuildRequires:	glib2-devel >= 1:2.58.1
BuildRequires:	libpng-devel >= 2:1.4.8
BuildRequires:	pango-devel >= 1:1.28.7
%endif
%if %{with lua}
BuildRequires:	lua >= 5.1
BuildRequires:	lua-devel >= 5.1
%endif
%if %{with perl}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
%endif
%if %{with python}
BuildRequires:	python3
BuildRequires:	python3-devel
%endif
%if %{with ruby}
BuildRequires:	rpm-rubyprov
BuildRequires:	ruby-devel
%endif
%if %{with tcl}
BuildRequires:	tcl-devel
%endif
%if %{with rrd_graph}
Requires:	glib2 >= 1:2.58.1
%else
Requires:	glib2 >= 1:2.28.7
%endif
%{?with_rrd_graph:Requires:	libpng >= 2:1.4.8}
Requires:	libxml2 >= 1:2.7.8
%{?with_rrd_graph:Requires:	pango >= 1:1.28.7}
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
używane poprzez prosty skrypcik (shell lub Perl), frontendy czy inne
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
как из простых скриптов (shell, Perl, etc) или встроена в программы,
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

%package cached
Summary:	Data caching daemon for RRDtool
Summary(pl.UTF-8):	Demon pamięci podręcznej danych dla RRDtoola
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description cached
Data caching daemon for RRDtool.

%description cached -l pl.UTF-8
Demon pamięci podręcznej danych dla RRDtoola.

%package devel
Summary:	RRDtool development
Summary(pl.UTF-8):	Narzędzia programistyczne pakietu RRDtool
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão da librrd
Summary(ru.UTF-8):	RRDtool - Заголовки, необходимые для разработки
Summary(uk.UTF-8):	RRDtool - бібліотечні лінки та файли хедерів
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with rrd_graph}
Requires:	glib2-devel >= 1:2.58.1
%else
Requires:	glib2-devel >= 1:2.28.7
%endif
Requires:	libdbi-devel
Requires:	libwrap-devel
Requires:	libxml2-devel >= 1:2.7.8
%{?with_rrd_graph:Requires:	pango-devel >= 1:1.28.7}

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

%package doc
Summary:	RRDtool documentation
Summary(pl.UTF-8):	Dokumentacja do RRDtoola
Group:		Documentation
BuildArch:	noarch

%description doc
RRD is the Acronym for Round Robin Database. RRD is a system to store
and display time-series data (i.e. network bandwidth, machine-room
temperature, server load average).

This package contains documentation on using RRD.

%description doc -l pl.UTF-8
RRD jest akronimem Round Robin Database. Jest to system pozwalający na
składowanie i wyświetlanie czasowych serii danych (np. przepustowość
sieci, temperatura w pomieszczeniu, obciążenie serwera).

Ten pakiet zawiera dokumentację użytkownika dla RRD.

%package -n lua-rrdtool
Summary:	RRD module for Lua
Summary(pl.UTF-8):	Moduł RRD dla języka Lua
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	lua

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

%package -n python3-rrdtool
Summary:	Python 3 interface to RRDtool
Summary(pl.UTF-8):	Pythonowy interfejs do RRDtoola
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs
Obsoletes:	python-rrdtool

%description -n python3-rrdtool
Python 3 interface to RRDtool, the graphing and logging utility.

%description -n python3-rrdtool -l pl.UTF-8
Interfejs Pythona 3 do RRDtoola - narzędzia do tworzenia wykresów i
logowania.

%package -n ruby-rrdtool
Summary:	Ruby interface to RRDtool
Summary(pl.UTF-8):	Interfejs języka Ruby do RRDtoola
Group:		Development/Languages/Ruby
Requires:	%{name} = %{version}-%{release}

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
%patch1 -p1

%{__sed} -i -e 's#\$TCL_PACKAGE_PATH#%{_prefix}/lib#g' configure.ac
%{__sed} -i -e 's#/lib/lua/#/%{_lib}/lua/#g' configure.ac

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
	examples/stripes.py

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+tclsh@TCL_VERSION@(\s|$),#!%{__tclsh}\1,' \
	bindings/tcl/ifOctets.tcl.in

# We only want .txt and .html files for the main documentation
install -d docs/{html,/txt}
%{__mv} doc/*.txt docs/txt
%{__mv} doc/*.html docs/html

# Put Perl docs in Perl package
install -d perl-docs/html
%{__mv} docs/html/RRD*.html perl-docs/html

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	--disable-silent-rules \
	%{__enable_disable static_libs static} \
	%{!?with_ceph:--disable-librados} \
	%{!?with_rrd_graph:--disable-rrd_graph} \
	%{!?with_rrdcgi:--disable-rrdcgi} \
	%{!?with_lua:--disable-lua} \
	%{!?with_perl:--disable-perl} \
	%{!?with_python:--disable-python} \
	%{!?with_ruby:--disable-ruby} \
	%{!?with_tcl:--disable-tcl} \
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
	pythondir=%{py3_sitedir} \
	examplesdir=%{_examplesdir}/%{name}-%{version} \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_archdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/librrd.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%if %{with lua}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lua/5.*/*.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/lua/5.*/*.a}
%endif

%if %{with perl}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/RRDs/.packlist
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS COPYRIGHT NEWS THREADS TODO
%attr(755,root,root) %{_libdir}/librrd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librrd.so.8
%{?with_rrdcgi:%attr(755,root,root) %{_bindir}/rrdcgi}
%attr(755,root,root) %{_bindir}/rrdcreate
%attr(755,root,root) %{_bindir}/rrdinfo
%attr(755,root,root) %{_bindir}/rrdtool
%attr(755,root,root) %{_bindir}/rrdupdate
%{_mandir}/man1/bin_dec_hex.1*
%{_mandir}/man1/cdeftutorial.1*
%{_mandir}/man1/rpntutorial.1*
%{_mandir}/man1/rrd-beginners.1*
%{_mandir}/man1/rrd_pdpcalc.1*
%{_mandir}/man1/rrdbuild.1*
%{?with_rrdcgi:%{_mandir}/man1/rrdcgi.1*}
%{_mandir}/man1/rrdcreate.1*
%{_mandir}/man1/rrddump.1*
%{_mandir}/man1/rrdfetch.1*
%{_mandir}/man1/rrdfirst.1*
%{_mandir}/man1/rrdgraph*.1*
%{_mandir}/man1/rrdinfo.1*
%{_mandir}/man1/rrdlast.1*
%{_mandir}/man1/rrdlastupdate.1*
%{_mandir}/man1/rrdlist.1*
%{?with_ceph:%{_mandir}/man1/rrdrados.1*}
%{_mandir}/man1/rrdresize.1*
%{_mandir}/man1/rrdrestore.1*
%{_mandir}/man1/rrdthreads.1*
%{_mandir}/man1/rrdtool.1*
%{_mandir}/man1/rrdtune.1*
%{_mandir}/man1/rrdtutorial.1*
%{_mandir}/man1/rrdupdate.1*
%{_mandir}/man1/rrdxport.1*

%files cached
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rrdcached
%{_mandir}/man1/rrdcached.1*
%{_mandir}/man1/rrdflushcached.1*
%{systemdunitdir}/rrdcached.service
%{systemdunitdir}/rrdcached.socket

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librrd.so
%{_includedir}/rrd*.h
%{_pkgconfigdir}/librrd.pc
%{_mandir}/man3/librrd.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a
%endif

%files doc
%defattr(644,root,root,755)
%doc docs/html docs/txt
%{_examplesdir}/%{name}-%{version}

%if %{with lua}
%files -n lua-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/5.*/rrd.so*
%{_mandir}/man1/rrdlua.1*
%endif

%if %{with perl}
%files -n perl-rrdtool
%defattr(644,root,root,755)
%doc perl-docs/html/*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%dir %{perl_vendorarch}/auto/RRDs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man3/RRDp.3*
%{_mandir}/man3/RRDs.3*
%endif

%if %{with python}
%files -n python3-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/rrdtool*.so
%{py3_sitedir}/rrdtool-*.egg-info
%{_mandir}/man1/rrdpython.1*
%endif

%if %{with ruby}
%files -n ruby-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/RRD.so
%{_mandir}/man1/rrdruby.1*
%endif

%if %{with tcl}
%files -n tcl-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclrrd%{version}.so
%{_prefix}/lib/tclrrd%{version}
%endif
