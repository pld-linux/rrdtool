%include        /usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Name:		rrdtool
Version:	1.0.28
Release:	1
License:	GPL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	http://ee-staff.ethz.ch/~oetiker/webtools/rrdtools/pub/%{name}-%{version}.tar.gz
#Patch0:	/%{name}-perl-location.patch
Patch0:		%{name}-makefile.patch
URL:		http://ee-staff.ethz.ch/~oetiker/webtools/rrdtol/
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
%patch -p1

%build
aclocal
automake
autoconf
%configure \
	--enable-shared=yes \
	--without-tclib
# uncoment this line ONLY IF tcl package is ready. 
#	--with-tclib=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} DESTDIR=$RPM_BUILD_ROOT site-perl-install

install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

(cd $RPM_BUILD_ROOT/usr/src/examples/%{name};
mv ../../../examples/* .;
mv ../../../contrib .)

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_bindir}/trytime
%attr(755,root,root) %{_libdir}/librrd.so.0.0.0
%{_libdir}/perl
%{_mandir}/man1/*

%files devel
%attr(644,root,root) %{_libdir}/librrd.so
%{_examplesdir}/%{name}

%files static
%attr(755,root,root) %{_libdir}/librrd.la
%{_libdir}/librrd.a
