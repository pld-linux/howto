Summary: Various HOWTOs from the Linux Documentation Project
Name: howto
Version: 1.0
Release: 1
Group: Documentation
Group: Dokumentacja
Source0: ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-HOWTOs.tar.gz
Source1: ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-mini-HOWTOs.tar.gz
Copyright: distributable
BuildRoot: /tmp/%{name}-%{version}-root
BuildArchitectures: noarch
Obsoletes: ldp
Vendor: LDP Project 

%description
This is the best collection of Linux documentation there is.  It
was put together on Apr 15 1998.  If you want to find newer
versions of these documents, see http://sunsite.unc.edu/linux.
For the versions in this package, see /usr/doc/HOWTO.

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

%changelog
* Wed Jan 14 1999 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
- null  
