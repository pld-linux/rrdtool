%include        /usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Name:		rrdtool
Version:	1.0.33
Release:	1
License:	GPL
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	http://ee-staff.ethz.ch/~oetiker/webtools/rrdtools/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://ee-staff.ethz.ch/~oetiker/webtools/rrdtol/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequired:	tcl-devel
%requires_eq	perl
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
Summary:	RDDTools development
Summary(pl):	Narzêdzia programistyczne pakietu RRDtools
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}

%description devel
RDDTools development files.

%description -l pl devel
Narzêdzia programistyczne pakietu RRDtools.

%package static
Summary:	RDDTools static library
Summary(pl):	Statyczne biblioteki RRDtools
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel

%description static
RDDTools static library.

%description -l pl static
Statyczne biblioteki RRDtools.

%prep
%setup -q
%patch -p1

%build
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} DESTDIR=$RPM_BUILD_ROOT site-perl-install

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
%{_libdir}/perl
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librrd.so
%attr(644,root,root) %{_libdir}/librrd.la
%{_examplesdir}/%{name}

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librrd.la
%{_libdir}/librrd.a
