%include        /usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pl):	RRDtool - baza danych typu round-robin
Summary(pt_BR):	Round Robin Database, uma ferramenta para construção de gráficos
Name:		rrdtool
Version:	1.0.33
Release:	6
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
RRD jest akronimem Round Robin Database. Jest to system pozwalaj±cy na
sk³adowanie i wy¶wietlanie czasowych serii danych (np. przepustowo¶æ
sieci, temperatura w pomieszczeniu, obci±¿enie servera). Sk³aduje dane
w "skondensowanej" postaci, która nie rozrasta siê z biegiem czasu
oraz pozwala na produkowanie wykresów z u¿ytecznymi danymi. Mo¿e byæ
u¿ywane poprzez prosty skrypcik (shell lub perl), frontendy czy inne
interfejsy u¿ytkownika.

%description -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).
Os dados são armazenados em uma forma compacta que não se expande com
o tempo, e gráficos podem ser apresentados processando-se esses dados.
RRD pode ser utilizado com wrapper scripts (em shell ou Perl) ou
através de front-ends.

%package devel
Summary:	RDDTools development
Summary(pl):	Narzêdzia programistyczne pakietu RRDtools
Summary(pt_BR):	Bibliotecas e arquivos de inclusão da librrd
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
RDDTools development files.

%description devel -l pl
Narzêdzia programistyczne pakietu RRDtools.

%description devel -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).

Este pacote contem arquivos de desenvolvimento do RRD.

%package static
Summary:	RDDTools static library
Summary(pl):	Statyczne biblioteki RRDtools
Summary(pt_BR):	Biblioteca estática librrd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
RDDTools static library.

%description static -l pl
Statyczne biblioteki RRDtools.

%description static -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilização de rede, temperaturas, cargas em servidores).

Este pacote contem a biblioteca estática do RRD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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
