Summary: RRDtool - round robin database
Name: rrdtool
Version: 1.0.6
Release: 0
Copyright: GPL
Group: Applications/Databases
Source0: http://www.caida.org/Tools/RRDtool/pub/rrdtool-1.0.6.tar.gz
Patch0: /rrdtool-perl-location.patch
Buildroot: /var/tmp/rrdtool-root
Prefix: /usr
Packager: Ragnar Kjørstad <rrdtool@ragnark.vestdata.no>
Url: http://www.caida.org/Tools/RRDtool/
Vendor: Tobi Oetiker <oetiker@ee.ethz.ch>

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
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix="/usr" 
make

%install
make install PREFIX=$RPM_BUILD_ROOT/usr

%files
/usr/bin/rrdtool
/usr/bin/rrdcgi
%doc /usr/man/man3/RRDp.3
%doc /usr/man/man3/RRDs.3
%doc /usr/man/man1/bin_dec_hex.1
%doc /usr/man/man1/rrdcgi.1
%doc /usr/man/man1/rrdcreate.1
%doc /usr/man/man1/rrddump.1
%doc /usr/man/man1/rrdfetch.1
%doc /usr/man/man1/rrdgraph.1
%doc /usr/man/man1/rrdlast.1
%doc /usr/man/man1/rrdresize.1
%doc /usr/man/man1/rrdrestore.1
%doc /usr/man/man1/rrdtool.1
%doc /usr/man/man1/rrdtune.1
%doc /usr/man/man1/rrdtutorial.1
%doc /usr/man/man1/rrdupdate.1
%doc doc/*.txt
%doc doc/*.html
/usr/lib/perl/auto/RRDs/RRDs.bs
/usr/lib/perl/auto/RRDs/RRDs.so
/usr/lib/perl/RRDp.pm
/usr/lib/perl/RRDs.pm
%doc examples/piped-demo.pl
%doc examples/shared-demo.pl
%doc examples/cgi-demo.cgi
%doc contrib
