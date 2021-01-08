%global debug_package %{nil}
%define soname 1
Name:           librdkafka
Version:        1.4.0
Release:        1%{?dist}
Summary:        The Apache Kafka C library
Group:          Development/Libraries/C and C++
License:        BSD-2-Clause
URL:            https://github.com/edenhill/librdkafka
Source0:	    librdkafka-%{version}.tar.gz
BuildRequires:  zlib-devel 
BuildRequires:  libstdc++-devel 
BuildRequires:  gcc >= 4.1 
BuildRequires:  openssl-devel 
BuildRequires:  cyrus-sasl
BuildRequires:  python2
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%define _source_payload w9.gzdio
%define _binary_payload w9.gzdio

%description
librdkafka is the C/C++ client library implementation of the Apache Kafka protocol, containing both Producer and Consumer support.


%package -n     %{name}%{soname}
Summary:        The Apache Kafka C library
Group:          Development/Libraries/C and C++
Requires:       zlib libstdc++ cyrus-sasl
Requires:       openssl

%description -n %{name}%{soname}
librdkafka is the C/C++ client library implementation of the Apache Kafka protocol, containing both Producer and Consumer support.

%package -n     %{name}-devel
Summary:        The Apache Kafka C library (Development Environment)
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
librdkafka is the C/C++ client library implementation of the Apache Kafka protocol, containing both Producer and Consumer support.
This package contains headers and libraries required to build applications
using librdkafka.


%prep
%setup -q -n %{name}-%{version}

# --install-deps will install missing dependencies that are not available
# through BuildRequires, such as libzstd, which will be linked statically.
%configure --install-deps --disable-lz4-ext

%build
cat config.log
make
examples/rdkafka_example -X builtin.features

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install

%clean
rm -rf %{buildroot}

%post   -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(444,root,root)
%{_libdir}/librdkafka.so.%{soname}
%{_libdir}/librdkafka++.so.%{soname}
%defattr(-,root,root)
%doc %{_docdir}/librdkafka/README.md 
%doc %{_docdir}/librdkafka/CONFIGURATION.md 
%doc %{_docdir}/librdkafka/INTRODUCTION.md 
%doc %{_docdir}/librdkafka/STATISTICS.md
%doc %{_docdir}/librdkafka/LICENSE 
%doc %{_docdir}/librdkafka/LICENSES.txt

%defattr(-,root,root)
#%{_bindir}/rdkafka_example
#%{_bindir}/rdkafka_performance

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/librdkafka
%defattr(444,root,root)
%{_libdir}/librdkafka.a
%{_libdir}/librdkafka.so
%{_libdir}/librdkafka++.a
%{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka++.pc
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka-static.pc
%{_libdir}/pkgconfig/rdkafka++-static.pc

%changelog
*   Mon Jan 04 2021 Henry Li <lihl@microsoft.com> 1.2.0-1
-   Initial CBL-Mariner import (license: BSD-2-Clause).
*   Thu Apr 09 2015 Eduard Iskandarov <e.iskandarov@corp.mail.ru> 0.8.6-0
-   0.8.6 simplify build process
*   Fri Oct 24 2014 Magnus Edenhill <rdkafka@edenhill.se> 0.8.5-0
-   0.8.5 release
*   Mon Aug 18 2014 Magnus Edenhill <rdkafka@edenhill.se> 0.8.4-0
-   0.8.4 release
*   Mon Mar 17 2014 Magnus Edenhill <vk@edenhill.se> 0.8.3-0
-   Initial RPM package
