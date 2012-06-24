%include	/usr/lib/rpm/macros.perl
Summary:	RRDtool - round robin database
Summary(pl):	RRDtool - baza danych typu round-robin
Summary(pt_BR):	Round Robin Database, uma ferramenta para constru��o de gr�ficos
Summary(ru):	RRDtool - ���� ������ � "����������� �����������"
Summary(uk):	RRDtool - �� ������� ���Ҧ����� �� ������ ��Ҧ���� �����
Name:		rrdtool
Version:	1.2.12
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/%{name}-%{version}.tar.gz
# Source0-md5:	7b544c38a818cbebcf06fe39b9f52d0d
Patch0:		%{name}-tcl-path.patch
URL:		http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.7
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libpng-devel >= 2:1.2.8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel >= 1.2.1
Requires:	libart_lgpl >= 2.3.17
Requires:	libpng >= 1.2.8
Requires:	zlib >= 1.2.1
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
RRD jest akronimem Round Robin Database. Jest to system pozwalaj�cy na
sk�adowanie i wy�wietlanie czasowych serii danych (np. przepustowo��
sieci, temperatura w pomieszczeniu, obci��enie serwera). Sk�aduje dane
w "skondensowanej" postaci, kt�ra nie rozrasta si� z biegiem czasu
oraz pozwala na produkowanie wykres�w z u�ytecznymi danymi. Mo�e by�
u�ywane poprzez prosty skrypcik (shell lub perl), frontendy czy inne
interfejsy u�ytkownika.

%description -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utiliza��o de rede, temperaturas, cargas em servidores).
Os dados s�o armazenados em uma forma compacta que n�o se expande com
o tempo, e gr�ficos podem ser apresentados processando-se esses dados.
RRD pode ser utilizado com wrapper scripts (em shell ou Perl) ou
atrav�s de front-ends.

%description -l ru
RRD - ��������� ��� "Round Robin Database" (���� ������ � "�����������
�����������"). RRD - ������� ��� ���������� � ������ ���������� ��
������������ ���������� ������� (�������� �������� �������� ������ �
����, ����������� � �������� ����, ������� �������� �������). ���
��������� ������ � ����� ���������� �����, ��� ��� ������ �� �����
�������� ��� ������ � ������ ����� � �������� ������� � �������������
�������� ����������� ������������� ����������. ����� ���� ������������
��� �� ������� �������� (shell, perl, etc) ��� �������� � ���������,
������� ���������� ������� ���������� � ���������� ������ � �������
��� ������������ ����.

%description -l uk
����� RRD - �� ����Φ� ��� Round Robin Database. RRD - �� �������
���Ҧ����� �� ������ ��Ҧ���� ����� (���������, ������ ������,
����������� ���������, ������������ �������). RRD ���Ҧ��� ��Φ ����
��������� � ���, �� ���ͦ� ���� ����� �� �¦���դ���� � �����, ��
�������դ �����Φ ���Ʀ�� ���������� ��Φ � ���, ��� ����������
���Ҧ��� ݦ��Φ��� ��¦��� � ��Ӧ. RRD ����� ��������������� �� �����
����Ԧ wrapper-�������, ��� � ����� ���������, �� �������� ������צ
������ϧ �� ������� ����Φ� ��������� �����������.

%package devel
Summary:	RRDtool development
Summary(pl):	Narz�dzia programistyczne pakietu RRDtool
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o da librrd
Summary(ru):	RRDtool - ���������, ����������� ��� ����������
Summary(uk):	RRDtool - ¦�̦����Φ ̦��� �� ����� ����Ҧ�
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cgilibc-devel >= 0.5
Requires:	freetype-devel >= 2.1.7
Requires:	libart_lgpl-devel >= 2.3.17
Requires:	libpng-devel >= 2:1.2.8
Requires:	zlib-devel >= 1.2.1

%description devel
RRDtool development files.

%description devel -l pl
Narz�dzia programistyczne pakietu RRDtool.

%description devel -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utiliza��o de rede, temperaturas, cargas em servidores).

Este pacote contem arquivos de desenvolvimento do RRD.

%description devel -l ru
RRD - ��������� ��� "Round Robin Database" (���� ������ � "�����������
�����������"). RRD - ������� ��� ���������� � ������ ���������� ��
������������ ���������� ������� (�������� �������� �������� ������ �
����, ����������� � �������� ����, ������� �������� �������).

���� ����� ��������� ��������� ���������, ������� ���������� ���
���������� ���������������.

%description devel -l uk
RRDtool - ������������ ����� � ����� �������.

%package static
Summary:	RRDtool static library
Summary(pl):	Statyczne biblioteki RRDtool
Summary(pt_BR):	Biblioteca est�tica librrd
Summary(ru):	RRDtool - ����������� ����������
Summary(uk):	������Φ ¦�̦����� RRDtool
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
RRDtool static library.

%description static -l pl
Statyczne biblioteki RRDtool.

%description static -l pt_BR
RRD e' um sistema para armazenar e apresentar series temporais de
dados (i.e. utiliza��o de rede, temperaturas, cargas em servidores).

Este pacote contem a biblioteca est�tica do RRD.

%description static -l ru
RRD - ��������� ��� "Round Robin Database" (���� ������ � "�����������
�����������"). RRD - ������� ��� ���������� � ������ ���������� ��
������������ ���������� ������� (�������� �������� �������� ������ �
����, ����������� � �������� ����, ������� �������� �������). ����
����� ��������� ��������� ���������� ������������ ���������, �������
���������� ��� ���������� ���������������.

%description static -l uk
������Φ ¦�̦����� ��� �������� �������, �� �������������� RRDtool.

%package -n perl-rrdtool
Summary:	Access RRDtool from Perl
Summary(pl):	Dost�p do RRDtoola z poziomu Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-rrdtool
Perl modules to access RRDtool: RRDs to access RRDtool as shared
module and RRDp to access RRDtool via a set of pipes.

%description -n perl-rrdtool -l pl
Modu�y Perla pozwalaj�ce na dost�p do RRDtoola: RRDs do dost�pu do
RRDtoola jako modu�u dzielonego oraz RRDp do dost�pu poprzez zestaw
potok�w.

%package -n python-rrdtool
Summary:	Python interface to RRDtool
Summary(pl):	Pythonowy interfejs do RRDtoola
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-rrdtool
Python interface to RRDtool, the graphing and logging utility.

%description -n python-rrdtool -l pl
Interfejs Pythona do RRDtoola - narz�dzia do tworzenia wykres�w i
logowania.

%package -n tcl-rrdtool
Summary:	Tcl extension to access the RRD library
Summary(pl):	Rozszerzenie Tcl-a pozwalaj�ce na dost�p do biblioteki Tcl
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl

%description -n tcl-rrdtool
Tcl extension to access the RRD library.

%description -n tcl-rrdtool -l pl
Rozszerzenie Tcl-a pozwalaj�ce na dost�p do biblioteki Tcl.

%prep
%setup -q
%patch0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-latin2 \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	perl_sitearch=%{perl_vendorarch} \
	pythondir=%{py_sitedir} \
	examplesdir=%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_prefix}/{doc,html}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS NEWS README THREADS TODO doc/*.html
%attr(755,root,root) %{_bindir}/rrd*
%attr(755,root,root) %{_libdir}/librrd.so.*.*.*
%attr(755,root,root) %{_libdir}/librrd_th.so.*.*.*
%{_datadir}/rrdtool
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librrd.so
%attr(644,root,root) %{_libdir}/librrd_th.so
%{_libdir}/librrd.la
%{_libdir}/librrd_th.la
%{_includedir}/rrd.h
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/librrd.a
%{_libdir}/librrd_th.a

%files -n perl-rrdtool
%defattr(644,root,root,755)
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%dir %{perl_vendorarch}/auto/RRDs
%{perl_vendorarch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man3/RRDp.3*
%{_mandir}/man3/RRDs.3*

%files -n python-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/rrdtoolmodule.so

%files -n tcl-rrdtool
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclrrd%{version}.so
/usr/lib/tclrrd%{version}
