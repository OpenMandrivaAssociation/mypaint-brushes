%global mypaint_data_version 1.0

Name: mypaint-brushes
Version: 1.3.0
Release: 1
Summary: Brushes to be used with the MyPaint library

# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0
License: CC0
URL: https://github.com/Jehan/mypaint-brushes
Source0: https://github.com/Jehan/mypaint-brushes/archive/v%{version}.tar.gz#/mypaint-brushes-%{version}.tar.gz
Group: Graphics

BuildArch: noarch

BuildRequires: autoconf
BuildRequires: automake


%package devel
Summary: Files for developing with mypaint-brushes
Requires: pkgconfig
License: GPLv2+


%description
This package contains brush files for use with MyPaint and other programs.


%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.


%prep
%setup -q


%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std


%files
%doc AUTHORS NEWS README.md COPYING Licenses.dep5 Licenses.md
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/%{mypaint_data_version}
%{_datadir}/mypaint-data/%{mypaint_data_version}/brushes
# (tv) temp fix b/c of rpmlint rejecting the pkg:
#exclude %{_datadir}/mypaint-data/1.0/brushes/ramon/100\%_Opaque*


%files devel
%doc COPYING Licenses.dep5 Licenses.md
%{_datadir}/pkgconfig/mypaint-brushes-%{mypaint_data_version}.pc



