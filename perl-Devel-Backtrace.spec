%define upstream_name    Devel-Backtrace
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Object-oriented backtrace
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(String::Escape)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This class is a nice way to access all the information caller provides on a
given level.  It is used by L<Devel::Backtrace>, which generates an array of
all trace points.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 654920
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 401668
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jan 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.12-1mdv2009.1
+ Revision: 334748
- update to new version 0.12

* Tue Jul 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 232735
- update to new version 0.11

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
+ Revision: 193799
- update to new version 0.10

* Wed Feb 06 2008 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2008.1
+ Revision: 163046
- import perl-Devel-Backtrace


