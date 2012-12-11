%define upstream_name    Devel-REPL
%define upstream_version 1.003012

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	A modern perl interactive shell
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B::Keywords)
BuildRequires:	perl(Data::Dump::Streamer)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Lexical::Persistence)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(MooseX::AttributeHelpers)
BuildRequires:	perl(MooseX::Object::Pluggable)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Sys::SigAction)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Term::ReadLine)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/re.pl

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1:1.3.12-2mdv2011.0
+ Revision: 656907
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.12-1mdv2011.0
+ Revision: 596607
- update to 1.003012

* Mon Sep 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.11-2mdv2011.0
+ Revision: 581245
- use meta.yml for deps

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.11-1mdv2011.0
+ Revision: 553123
- update to 1.003011

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.9-1mdv2010.1
+ Revision: 517311
- adding missing buildrequires:
- update to 1.003009

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.7-1mdv2010.1
+ Revision: 504835
- bump epoch
- rebuild using %%perl_convert_version

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003007-1mdv2010.0
+ Revision: 391942
- update to new version 1.003007

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.003006-1mdv2010.0
+ Revision: 369664
- update to new version 1.003006

* Mon Feb 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.003004-1mdv2009.1
+ Revision: 340731
- update to new version 1.003004

* Sun Feb 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.003003-1mdv2009.1
+ Revision: 338448
- update to new version 1.003003

* Fri Jan 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.003002-1mdv2009.1
+ Revision: 333055
- adding missing prereq for new version
- update to new version 1.003002

* Mon Jan 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.003001-1mdv2009.1
+ Revision: 328494
- new version

* Thu Dec 04 2008 Jérôme Quelin <jquelin@mandriva.org> 1.002001-1mdv2009.1
+ Revision: 309973
- import perl-Devel-REPL


* Thu Dec 04 2008 cpan2dist 1.002001-1mdv
- initial mdv release, generated with cpan2dist

