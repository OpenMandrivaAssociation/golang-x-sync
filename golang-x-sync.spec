# Run tests in check section
%bcond_without check

%bcond_without bootstrap2

# https://golang.org/x/sync
%global goipath		golang.org/x/sync
%global forgeurl	https://golang.org/x/sync
Version:			0.6.0

%gometa

Summary:	Supplemental Go packages for synchronization
Name:		golang-x-sync

Release:	1
Source0:	https://github.com/golang/sync/archive/v%{version}/sync-%{version}.tar.gz
%if %{with bootstrap2}
# Generated from Source100
Source3:	vendor.tar.zst
Source100:	golang-package-dependencies.sh
%endif
URL:		https://github.com/golang/sync
License:	BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
This package provides Go concurrency primitives in addition
to the ones provided by the language and "sync" and "sync/atomic"
packages.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE PATENTS
%doc CONTRIBUTING.md README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n sync-%{version}

rm -rf vendor

%if %{with bootstrap2}
tar xf %{S:3}
%endif

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

