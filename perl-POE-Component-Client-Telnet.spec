#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Client-Telnet
Summary:	POE::Component::Client::Telnet - non-blocking POE interface to Net::Telnet
Summary(pl.UTF-8):   POE::Component::Client::Telnet - nieblokujący interfejs POE do Net::Telnet
Name:		perl-POE-Component-Client-Telnet
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	90eca1ffae98b57eb4db9b5cbd828db1
URL:		http://search.cpan.org/dist/POE-Component-Client-Telnet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-Net-Telnet
BuildRequires:	perl-POE >= 1:0.3100
BuildRequires:	perl-Test-Simple >= 0.32
%endif
Requires:	perl-POE >= 1:0.3100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::Telnet is a POE component that provides a
non-blocking wrapper around Net::Telnet, or any other module based on
Net::Telnet. Consult the Net::Telnet documentation for more details.

%description -l pl.UTF-8
POE::Component::Client::Telnet to komponent POE udostępniający
nieblokujący wrapper dla Net::Telnet lub dowolnego innego modułu
opartego na Net::Telnet. Szczegóły w dokumentacji Net::Telnet.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Client/Telnet.pm
%{_mandir}/man3/*
