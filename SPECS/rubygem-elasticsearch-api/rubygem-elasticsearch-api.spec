%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name elasticsearch-api

Name:           rubygem-elasticsearch-api
Version:        7.6.0
Release:        1%{?dist}
Summary:        Ruby API for Elasticsearch
Group:          Development/Languages
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby >= 2.4.0
Requires:       rubygem-multi_json

%description
The elasticsearch-api library provides a Ruby implementation of the Elasticsearch REST API.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
*   Wed Jan 06 2021 Henry Li <lihl@microsoft.com> 7.6.0-1
-   Original version for CBL-Mariner.
-   License verified.
