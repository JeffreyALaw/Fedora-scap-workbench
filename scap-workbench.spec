%{?scl:%scl_package scap-workbench}
%{!?scl:%global pkg_name scap-workbench}

%{?scl:%global _scl_prefix /opt/scap-testing}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		%{?scl_prefix}scap-workbench
Version:	0.8.5
Release:	1%{?dist}
Summary:	Scanning, tailoring, editing and validation tool for SCAP content

License:	GPLv3+
URL:		https://fedorahosted.org/scap-workbench/
Source0:	https://fedorahosted.org/released/scap-workbench/%{pkg_name}-%{version}.tar.bz2
Group:		System Environment/Base

BuildRequires:	cmake
BuildRequires:	qt-devel
BuildRequires:	qtwebkit-devel

BuildRequires:	%{?scl_prefix}openscap-devel >= 0.9.13
BuildRequires:	%{?scl_prefix}openscap-utils >= 0.9.13
Requires:		%{?scl_prefix}openscap-utils >= 0.9.13
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
%cmake -D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/scap-workbench
%{_datadir}/applications/scap-workbench.desktop
%{_datadir}/pixmaps/scap-workbench.png
%doc %{_mandir}/man8/scap-workbench.8.gz
%doc %{_pkgdocdir}/user_manual.html

%changelog
* Fri Jan 10 2014 Martin Preisler <mpreisle@redhat.com> 0.8.5-1
- Updated to new version

* Mon Dec 09 2013 Martin Preisler <mpreisle@redhat.com> 0.8.4-1
- Updated to new version

* Fri Nov 29 2013 Martin Preisler <mpreisle@redhat.com> 0.8.3-1
- Updated to new version
- Added measures to deal with unversioned pkgdocdir in Fedora 20+

* Mon Nov 18 2013 Martin Preisler <mpreisle@redhat.com> 0.8.2-2
- Removed the openscap detection workaround, it is no longer needed with openscap 0.9.13

* Wed Oct 30 2013 Martin Preisler <mpreisle@redhat.com> 0.8.2-1
- Updated to new version
- Added a workaround to the cmake invocation because of faulty openscap .pc file

* Fri Sep 20 2013 Martin Preisler <mpreisle@redhat.com> 0.8.1-1
- Updated to new version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Martin Preisler <mpreisle@redhat.com> 0.8.0-1
- Initial release of the rewritten workbench
