Summary:	RRDtool - round robin database
Name:		rrdtool
Version:	1.0.28
Release:	1
License:	GPL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	http://ee-staff.ethz.ch/~oetiker/webtools/rrdtools/pub/%{name}-%{version}.tar.gz
#Patch0:	/%{name}-perl-location.patch
#Url:		http://www.caida.org/tools/utilites/rrdtool/
URL:		http://ee-staff.ethz.ch/~oetiker/webtools/rrdtol/
#Vendor:	Tobi Oetiker <oetiker@ee.ethz.ch>
#BuildRequired:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store
and display time-series data (i.e. network bandwidth, machine-room
temperature, server load average). It stores the data in a very
compact way that will not expand over time, and it presents useful
graphs by processing the data to enforce a certain data density. It
can be used either via simple wrapper scripts (from shell or Perl) or
via frontends that poll network devices and put a friendly user
interface on it.

%package devel
Summary:	RDDTools development.
Summary(pl):	Na¿êdzia programistyczne pakietu RRDtools
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}
%description devel
%description -l pl devel

%package static
Summary:	RDDTools static library.
Summary(pl):	Statycznie linkowana biblioteka RRDtools.
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel
%description static
%description -l pl static

%prep
%setup -q
#%patch0 -p1
#mv contrib/log2rrd/log2rrd.pl contrib/log2rrd/log2rrd.pl.in

%build
aclocal
autoconf
%configure --prefix=%{_prefix} \
	--enable-shared=yes \
	--without-tclib
# uncoment this line ONLY IF tcl package is ready. 
#	--with-tclib=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} imandir=%{_mandir} DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}/contrib
(cd $RPM_BUILD_ROOT/usr/src/examples/%{name};
cp -Rp ../../../examples/* .;
cp -Rp ../../../contrib .)

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%doc doc/*.html
%doc doc/*.pod

%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_bindir}/trytime

%attr(644,root,root) %{_libdir}/librrd.so
%attr(755,root,root) %{_libdir}/librrd.so.0.0.0

%dir %{_libdir}/perl
%attr(644,root,root) %{_mandir}/man/man1/*

%files static
%attr(644,root,root) %{_libdir}/librrd.a
%attr(755,root,root) %{_libdir}/librrd.la

%files devel
%attr(644,root,root) %{_libdir}/librrd.so.0
%dir %{_examplesdir}/%{name}
