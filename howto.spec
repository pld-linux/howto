Summary:	Various HOWTOs from the Linux Documentation Project
Summary(pl):	Rozmaite dokumenty HOWTO z Linux Documentation Project
Name:		howto
Version:	20020131
Release:	1
License:	distributable
Group:		Documentation
Group(de):	Dokumentation
Group(pl):	Dokumentacja
Source0:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-HOWTOs-%{version}.tar.gz
Source1:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/mini/Linux-mini-HOWTOs-%{version}.tar.gz 
BuildArch:	noarch
Obsoletes:	ldp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux HOWTOs are detailed documents which describe a specific aspect of
configuring or using Linux. Linux HOWTOs are a great source of practical
information about your system. The latest versions of these documents are
located at http://www.linuxdoc.org/docs.html#howto

%description -l fr                                                                                            
Les HOWTO Linux sont des documents d�crivant de fa�on exhaustive un aspect
de la configuration ou de l'utilisation d'un syst�me Linux. Les HOWTO Linux
sont l'une des meilleures sources d'information sur la pratique de votre
syst�me. La derni�re version de chacun de ces documents peut �tre touv�e �
cette adresse: http://www.linuxdoc.org/docs.html#howto

%description -l pl
To jest zbi�r dokument�w HOWTO, w kt�rych znajdziesz odpowiedzi na
du�� cz�� pyta� pojawiaj�cych si� przy pracy z Linuxem.
Najnowsze wersje tych dokument�w znajdziesz pod adresem:
http://www.linuxdoc.org/docs.html#howto

%prep 
%setup -qc
%setup -qcT -a1 -n %{name}-%{version}/mini
%setup -qDT -n %{name}-%{version}

%build
find . -type f | xargs gzip -9  

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_defaultdocdir}/HOWTO/text

cp -ar *    $RPM_BUILD_ROOT%{_defaultdocdir}/HOWTO/text 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/HOWTO/text/
