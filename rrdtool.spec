Summary: 	RRDtool - round robin database
Name: 		rrdtool
Version: 	1.0.13
Release: 	1
Copyright: 	GPL
Group: 		Applications/Databases
Source0: 	http://www.caida.org/tools/utilites/rrdtool/pub/%{name}-%{version}.tar.gz
#Patch0: 	/rrdtool-perl-location.patch
Url: 		http://www.caida.org/tools/utilites/rrdtool/
Vendor: 	Tobi Oetiker <oetiker@ee.ethz.ch>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and 
display time-series data (i.e. network bandwidth, machine-room temperature, 
server load average). It stores the data in a very compact way that will not 
expand over time, and it presents useful graphs by processing the data to 
enforce a certain data density. It can be used either via simple wrapper 
scripts (from shell or Perl) or via frontends that poll network devices and 
put a friendly user interface on it.

%prep
%setup -q
#%patch0 -p1
#mv contrib/log2rrd/log2rrd.pl contrib/log2rrd/log2rrd.pl.in

%build
aclocal
autoconf
%configure
%{__make}

%install
%{__make} install PREFIX=$RPM_BUILD_ROOT/usr

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%doc doc/*.html
%doc examples/piped-demo.pl
%doc examples/shared-demo.pl
%doc examples/cgi-demo.cgi
%doc contrib

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*

/usr/lib/perl/auto/RRDs/RRDs.bs
/usr/lib/perl/auto/RRDs/RRDs.so
/usr/lib/perl/RRDp.pm
/usr/lib/perl/RRDs.pm
