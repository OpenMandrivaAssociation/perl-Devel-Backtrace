
%define realname   Devel-Backtrace
%define version    0.11
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Object-oriented backtrace
Source:     http://www.cpan.org/modules/by-module/Devel/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(String::Escape)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
This class is a nice way to access all the information caller provides on a
given level.  It is used by L<Devel::Backtrace>, which generates an array of
all trace points.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*



