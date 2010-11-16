%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary: Enlightenment Input Output Library
Name: eio
Version: 0.1.0.54504
Release: %mkrel 1
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source: http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: eina-devel >= 1.0.0
BuildRequires: ecore-devel >= 1.0.0

%description
This library is intended to provide non blocking IO by using thread for all
operation that may block. It depends only on eina and ecore right now. It
should integrate all the features/functions of Ecore_File that could block.

This should become one day part of what we call the EFL and be a dependence
of E17. Feel free to contribute, help is always appreciated !

%package -n %libname
Summary: Enlightenment Input Output Library
Group: System/Libraries

%description -n %libname
Enlightenment Input Output Library.

%package -n %develname
Summary: Enlightenment Input Output Library - devel files
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
eio development headers and development libraries.

%prep
%setup -q -n %name-%version

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

find %buildroot -name *.la | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
