%global goipath         github.com/git-lfs/go-netrc
%global commit          e0e9ca483a183481412e6f5a700ff20a36177503

%gometa

# Hack to match name that will exist when Go macros are updated.
%global goname golang-github-git-lfs-netrc

%global common_description %{expand:
A Golang package for reading and writing netrc files. This package can
parse netrc files, make changes to them, and then serialize them back to
netrc format, while preserving any whitespace that was present in the
source file.}

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A Golang package for reading and writing netrc files
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jun 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.gite0e9ca4
- Initial package for Fedora
