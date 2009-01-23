%define realname   Devel-REPL
%define version    1.003002
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Read lines until all blocks are closed
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/Devel/%{realname}-%{version}.tar.gz
BuildRequires: perl(B::Keywords)
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Lexical::Persistence)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(MooseX::Object::Pluggable)
BuildRequires: perl(PPI)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Colors are very pretty.

This plugin causes certain prints, warns, and errors to be colored.
Generally the return value(s) of each line will be colored green (you can
override this by setting '$_REPL->normal_color' in your rcfile). Warnings
and compile/runtime errors will be colored with '$_REPL->error_color'. This
plugin uses the Term::ANSIColor manpage, so consult that module for valid
colors. The defaults are actually 'green' and 'bold red'.


%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

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
