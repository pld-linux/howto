Summary:	Various HOWTOs from the Linux Documentation Project
Summary(pl):	Rozmaite dokumenty HOWTO z Linux Documentation Project
Name:		howto
Version:	1.0
Release:	2
Group:		Documentation
Group(pl):	Dokumentacja
Source0:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-HOWTOs.tar.gz
Source1:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-mini-HOWTOs.tar.gz
Copyright:	distributable
BuildArch:	noarch
Obsoletes:	ldp
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is the best collection of Linux documentation there is.  It
was put together on Apr 15 1998.  If you want to find newer
versions of these documents, see http://sunsite.unc.edu/linux.
For the versions in this package, see /usr/doc/HOWTO.

%description -l pl
To jest zbiór dokumentów HOWTO, w których znajdziesz odpowiedzi na du¿± czê¶æ
pytañ pojawiaj±cych siê przy pracy z Linuxem.

%prep 

%setup -q -c  
%setup1 -q -c -n %{name}-%{version}/mini 

%build
cd .. 
find . -type f | xargs gzip -9  

%install
install -d  $RPM_BUILD_ROOT/usr/doc/HOWTO/text

cp -ar *    $RPM_BUILD_ROOT/usr/doc/HOWTO/text 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/doc/HOWTO/text/
