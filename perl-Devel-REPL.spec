%define upstream_name    Devel-REPL
%define upstream_version 1.003011

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    a modern perl interactive shell
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Keywords)
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Lexical::Persistence)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(MooseX::Object::Pluggable)
BuildRequires: perl(PPI)
BuildRequires: perl(Sys::SigAction)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::clean)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or
testing of code without the need to create a temporary source code file.

Through a plugin system, many features are available on demand. You can
also tailor the environment through the use of profiles and run control
files, for example to pre-load certain Perl modules when working on a
particular project.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/re.pl
