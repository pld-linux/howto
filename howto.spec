Summary:	Various HOWTOs from the Linux Documentation Project
Summary(es):	Varios HOWTOs del Proyecto de Documentaci�n del Linux (LDP)
Summary(pl):	Rozmaite dokumenty HOWTO z Linux Documentation Project
Summary(pt_BR):	V�rios HOWTOs do Projeto de Documenta��o do Linux (LDP)
Name:		howto
Version:	20030706
Release:	1
License:	distributable
Group:		Documentation
Source0:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-HOWTOs-%{version}.tar.bz2
# Source0-md5:	6d2feb7a2647c967f7e73299b361c6bf
Source1:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/mini/Linux-mini-HOWTOs-%{version}.tar.bz2
# Source1-md5:	327598d1d81746b5c81686477e6c9870
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ldp

%description
Linux HOWTOs are detailed documents which describe a specific aspect
of configuring or using Linux. Linux HOWTOs are a great source of
practical information about your system. The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%description -l es
Esta es la mejor colecci�n existente de documentos Linux. Si deseas
encontrar las versiones m�s recientes de estos documentos mira en
http://sunsite.unc.edu/Linux. Las versiones en este paquete est�n
en el directorio /usr/share/doc/HOWTO.

%description -l fr
Les HOWTO Linux sont des documents d�crivant de fa�on exhaustive un
aspect de la configuration ou de l'utilisation d'un syst�me Linux. Les
HOWTO Linux sont l'une des meilleures sources d'information sur la
pratique de votre syst�me. La derni�re version de chacun de ces
documents peut �tre touv�e � cette adresse:
http://www.linuxdoc.org/docs.html#howto

%description -l pl
To jest zbi�r dokument�w HOWTO, w kt�rych znajdziesz odpowiedzi na
du�� cz�� pyta� pojawiaj�cych si� przy pracy z Linuxem. Najnowsze
wersje tych dokument�w znajdziesz pod adresem:
http://www.linuxdoc.org/docs.html#howto

%description -l pt_BR
Esta � a melhor cole��o existente de documentos Linux. Se voc�
deseja encontrar as vers�es mais recentes destes documentos
veja em http://sunsite.unc.edu/Linux. As vers�es neste pacote
est�o no diret�rio /usr/share/doc/HOWTO.

%prep
%setup -qc
%setup -qcT -a1 -n %{name}-%{version}/mini
%setup -qDT -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_defaultdocdir}/HOWTO/text

cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/HOWTO/text

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/HOWTO/text/
