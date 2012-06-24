%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Glue library for Nitro + Og
Summary(pl):	Biblioteka Glue dla Nitro + Og
Name:		ruby-Glue
%define tarname glue
Version:	0.20.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/5189/%{tarname}-%{version}.tgz
# Source0-md5:	58c1fee49ce2eca0b294a8399b9166ed
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Glue for Nitro + Og.

%description -l pl
Ten pakiet zawiera bibliotek� Glue dla Nitro + Og.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_examplesdir}/%{name}-%{version}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README CHANGELOG doc/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Glue
