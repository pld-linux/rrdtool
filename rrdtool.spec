%include        /usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pt_BR):	Round Robin Database, uma ferramenta para construÁ„o de gr·ficos
Name:		rrdtool
Version:	1.0.33
Release:	5
License:	GPL
Group:		Applications/Databases
Group(de):	Applikationen/Dateibanken
Group(pl):	Aplikacje/Bazy danych
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

%description -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaÁ„o de rede, temperaturas, cargas em servidores).
Os dados s„o armazenados em uma forma compacta que n„o se expande com
o tempo, e gr·ficos podem ser apresentados processando-se esses dados.
RRD pode ser utilizado com wrapper scripts (em shell ou Perl) ou
atravÈs de front-ends.

%package devel
Summary:	RDDTools development
Summary(pl):	NarzÍdzia programistyczne pakietu RRDtools
Summary(pt_BR):	Bibliotecas e arquivos de inclus„o da librrd
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
RDDTools development files.

%description -l pl devel
NarzÍdzia programistyczne pakietu RRDtools.

%description -l pt_BR devel
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaÁ„o de rede, temperaturas, cargas em servidores).

Este pacote contem arquivos de desenvolvimento do RRD.

%package static
Summary:	RDDTools static library
Summary(pl):	Statyczne biblioteki RRDtools
Summary(pt_BR):	Biblioteca est·tica librrd
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
RDDTools static library.

%description -l pl static
Statyczne biblioteki RRDtools.

%description -l pt_BR static
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utilizaÁ„o de rede, temperaturas, cargas em servidores).

Este pacote contem a biblioteca est·tica do RRD.

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
