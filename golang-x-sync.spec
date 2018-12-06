# Run tests in check section
%bcond_without check

%global goipath         golang.org/x/sync
%global forgeurl        https://github.com/golang/sync
%global commit          fd80eb99c8f653c847d294a001bdf2a3a6f768f5

%global common_description %{expand:
Go concurrency primitives.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Go concurrency primitives
License: BSD
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/net/context)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-golang-sync-devel = %{version}-%{release}
Obsoletes: golang-github-golang-sync-devel < 0-0.3.20180314gitfd80eb9
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md PATENTS CONTRIBUTORS CONTRIBUTING.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitfd80eb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180316gitfd80eb9
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171101gitfd80eb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171101gitfd80eb9
- Upstream GIT revision fd80eb9

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170517gitf52d181
- First package for Fedora

