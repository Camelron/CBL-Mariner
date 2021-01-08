%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name fluent-plugin-webhdfs

Name:           rubygem-fluent-plugin-webhdfs
Version:        1.2.4
Release:        1%{?dist}
Summary:        Hadoop WebHDFS output plugin for Fluentd 
Group:          Development/Languages
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires:  ruby > 2.1.0
Requires:       rubygem-fluentd
Requires:       rubygem-webhdfs >= 0.6.0

%description
Fluentd output plugin to write data into Hadoop HDFS over WebHDFS/HttpFs.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE.txt
%{gemdir}

%changelog
*   Mon Jan 04 2021 Henry Li <lihl@microsoft.com> 1.2.4-1
-   Original version for CBL-Mariner.
-   License verified.
