Summary:	Various HOWTOs from the Linux Documentation Project
Summary(es):	Varios HOWTOs del Proyecto de Documentación del Linux (LDP)
Summary(pl):	Rozmaite dokumenty HOWTO z Linux Documentation Project
Summary(pt_BR):	Vários HOWTOs do Projeto de Documentação do Linux (LDP)
Name:		howto
Version:	20060908
Release:	1
License:	distributable
Group:		Documentation
Source0:	ftp://metalab.unc.edu/pub/Linux/docs/HOWTO/Linux-HOWTOs-%{version}.tar.bz2
# Source0-md5:	fba4546d6b6499b7be4f8d3b85c2f23b
URL:		http://www.tldp.org/docs.html#howto
Requires:	LDP-base
Obsoletes:	ldp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux HOWTOs are detailed documents which describe a specific aspect
of configuring or using Linux. Linux HOWTOs are a great source of
practical information about your system. The latest versions of these
documents are located at <http://www.tldp.org/docs.html#howto>.

%description -l es
Esta es la mejor colección existente de documentos Linux. Si deseas
encontrar las versiones más recientes de estos documentos mira en
http://sunsite.unc.edu/Linux. Las versiones en este paquete están en
el directorio %{_docdir}/LDP.

%description -l fr
Les HOWTO Linux sont des documents décrivant de façon exhaustive un
aspect de la configuration ou de l'utilisation d'un système Linux. Les
HOWTO Linux sont l'une des meilleures sources d'information sur la
pratique de votre système. La dernière version de chacun de ces
documents peut être touvée à cette adresse:
<http://www.tldp.org/docs.html#howto>.

%description -l pl
To jest zbiór dokumentów HOWTO, w których znajdziesz odpowiedzi na
du¿± czê¶æ pytañ pojawiaj±cych siê przy pracy z Linuksem. Najnowsze
wersje tych dokumentów znajdziesz pod adresem:
<http://www.tldp.org/docs.html#howto>.

%description -l pt_BR
Esta é a melhor coleção existente de documentos Linux. Se você deseja
encontrar as versões mais recentes destes documentos veja em
<http://sunsite.unc.edu/Linux>. As versões neste pacote estão no
diretório %{_docdir}/LDP.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/text
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/text

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/text
