%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	E17 Input Output Library
Name:		eio
Version:	1.7.5
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(eet) >= 1.7.0
BuildRequires:	pkgconfig(ecore) >= 1.7.0
BuildRequires:	pkgconfig(eina) >= 1.7.0

%description
This library is intended to provide non blocking IO by using thread for all
operation that may block. It depends only on eina and ecore right now. It
should integrate all the features/functions of Ecore_File that could block.

This should become one day part of what we call the EFL and be a dependence
of E17. Feel free to contribute, help is always appreciated !

%package -n %{libname}
Summary:	Eio library
Group:		System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{devname}
Summary:	Eio headers, libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and libraries from %{name}

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS README ChangeLog NEWS
%{_includedir}/%{name}*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

