%define tarname glue
Summary:	Glue library for Nitro + Og
Summary(pl):	Biblioteka Glue dla Nitro + Og
Name:		ruby-Glue
Version:	0.25.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/7164/%{tarname}-%{version}.tgz
# Source0-md5:	98d61d4f04ec8feaf93971028b9dca90
URL:		http://rubyforge.org/projects/nitro/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Glue for Nitro + Og.

%description -l pl
Ten pakiet zawiera bibliotekê Glue dla Nitro + Og.

%prep
%setup -q -n %{tarname}

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
%doc rdoc README doc/*
%{ruby_rubylibdir}/*
%{ruby_ridir}/Glue
