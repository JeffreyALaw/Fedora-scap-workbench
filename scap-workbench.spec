%{?scl:%scl_package scap-workbench}
%{!?scl:%global pkg_name scap-workbench}

%{?scl:%global _scl_prefix /opt/scap-testing}

Name:		%{?scl_prefix}scap-workbench
Version:	0.8.0
Release:	1%{?dist}
Summary:	Scanning, tailoring, editing and validation tool for SCAP content

License:	GPLv3+
URL:		https://fedorahosted.org/scap-workbench/
Source0:	https://fedorahosted.org/released/scap-workbench/%{pkg_name}-%{version}.tar.bz2
Group:		System Environment/Base

BuildRequires:	cmake
BuildRequires:	qt-devel
BuildRequires:	qtwebkit-devel

# --progress was added in 0.9.5
BuildRequires:	%{?scl_prefix}openscap-devel >= 0.9.5
BuildRequires:	%{?scl_prefix}openscap-utils >= 0.9.5
Requires:		%{?scl_prefix}openscap-utils >= 0.9.5
# ssh to scan remote machines
Requires:		openssh-clients
# because of 'setsid' which we use to force ssh to use GUI askpass
Requires:		util-linux
%{?scl:Requires: %scl_runtime}

%description
scap-workbench is GUI tool that provides scanning functionality for SCAP
content. The tool is based on OpenSCAP library.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/scap-workbench
%{_mandir}/man8/scap-workbench.8.gz
%{_datadir}/pixmaps/scap-workbench.png

%changelog
* Thu Jul 04 2013 Martin Preisler <mpreisle@redhat.com> 0.8.0-1
- Initial release of the rewritten workbench
